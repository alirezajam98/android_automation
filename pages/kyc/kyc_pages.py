from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.interaction import Interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from conftest import driver
from pages.base_page import BasePage


class CreateAccountPage(BasePage):
    """کلاس مربوط به صفحه ایجاد حساب کاربری"""

    def click_create_account(self):
        create_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
        )
        create_account_button.click()


class OpenAccountPage(BasePage):
    """کلاس مربوط به صفحه باز کردن حساب"""

    def click_open_account(self):
        open_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openAccountButton"))
        )
        open_account_button.click()


class SelectServerPage(BasePage):
    """کلاس مربوط به صفحه انتخاب سرور"""

    def select_uat_server(self):
        uat_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                            'new UiSelector().className("android.view.ViewGroup").instance(3)'))
        )
        uat_button.click()


class CreateAccountInfoPage(BasePage):
    """کلاس مربوط به صفحه اطلاعات حساب کاربری"""

    def click_start(self):
        start_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirm"))
        )
        start_button.click()


class AcceptRulesAndRegulations(BasePage):
    def click_rules_and_regulations(self):
        """کلیک روی سوییچ قوانین و مقررات"""
        accept_switch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, 'android.widget.Switch'))
        )
        accept_switch.click()

    def click_confirm_button(self):
        """کلیک روی دکمه تایید"""
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirm"))
        )
        confirm_button.click()

        return EnterPhoneNumberPage(self.driver)

    def is_switch_on(self):
        """بررسی اینکه سوییچ قوانین روشن است یا خاموش"""
        accept_switch = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (AppiumBy.CLASS_NAME, 'android.widget.Switch'))
        )
        # بررسی وضعیت سوییچ با استفاده از خاصیت checked
        switch_status = accept_switch.get_attribute("checked")
        return switch_status == "true"  # اگر true باشد یعنی سوییچ روشن است

    def toggle_switch(self):
        """تغییر وضعیت سوییچ قوانین و مقررات"""
        current_status = self.is_switch_on()
        self.click_rules_and_regulations()  # تغییر وضعیت سوییچ
        new_status = not current_status  # وضعیت جدید باید معکوس شود
        return new_status


class EnterPhoneNumberPage(BasePage):
    """کلاس مربوط به وارد کردن شماره تلفن"""

    def enter_phone_number(self, phone_number):
        phone_number_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/phoneInputEditText"))
        )
        phone_number_field.send_keys(phone_number)

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class ReferralPage(BasePage):
    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


class NationalCodePage(BasePage):
    def enter_national_code(self, national_code):
        national_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.EditText"))
        )
        national_code_field.send_keys(national_code)

    def get_national_code_text(self):
        """دریافت متن فیلد کد ملی"""
        national_code_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nationalCodeInputEditText"))
        )
        return national_code_field.get_attribute("text")

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


import re  # برای استفاده از Regex


class BirthDatePage(BasePage):

    def perform_initial_scroll(self):
        """اسکرول اولیه برای فعال‌سازی تاریخ"""
        year_picker = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/year"))
        )
        self.scroll_down_year()  # اسکرول کوچک به پایین برای فعال‌سازی فیلد تاریخ

    def get_current_date(self):
        """دریافت تاریخ انتخاب‌شده به‌صورت 'YYYY/MM/DD'"""
        birth_date_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/birthdateInputEditText"))
        )
        raw_date = birth_date_field.get_attribute("text")  # دریافت تاریخ به فرمت '۱۳۸۰/۰۷/۲۸'

        if not raw_date:
            raise ValueError("تاریخی برای نمایش وجود ندارد. اسکرول اولیه انجام نشده است.")

        # حذف تمام کاراکترهای غیر عددی (مانند "روز" یا "ماه")
        clean_date = re.sub(r'[^0-9/]', '', raw_date)
        return clean_date  # تاریخ را به صورت YYYY/MM/DD برمی‌گرداند

    def set_year(self, target_year):
        """تنظیم سال در DatePicker"""
        self.perform_initial_scroll()  # اسکرول اولیه برای فعال‌سازی فیلد تاریخ

        while True:
            current_date = self.get_current_date()  # دریافت تاریخ فعلی
            current_year = int(current_date.split("/")[0])  # جدا کردن سال از تاریخ
            if current_year == target_year:
                break  # اگر سال موردنظر انتخاب شده است، از حلقه خارج شود
            if current_year < target_year:
                self.scroll_down_year()  # اسکرول به سمت پایین برای افزایش سال
            else:
                self.scroll_up_year()  # اسکرول به سمت بالا برای کاهش سال

    def set_month(self, target_month):
        """تنظیم ماه در DatePicker"""
        while True:
            current_date = self.get_current_date()  # دریافت تاریخ فعلی
            current_month = int(current_date.split("/")[1])  # جدا کردن ماه از تاریخ
            if current_month == target_month:
                break  # اگر ماه موردنظر انتخاب شده است، از حلقه خارج شود
            if current_month < target_month:
                self.scroll_down_month()  # اسکرول به سمت پایین برای افزایش ماه
            else:
                self.scroll_up_month()  # اسکرول به سمت بالا برای کاهش ماه

    def set_day(self, target_day):
        """تنظیم روز در DatePicker"""
        while True:
            current_date = self.get_current_date()  # دریافت تاریخ فعلی
            current_day = int(current_date.split("/")[2])  # جدا کردن روز از تاریخ
            if current_day == target_day:
                break  # اگر روز موردنظر انتخاب شده است، از حلقه خارج شود
            if current_day < target_day:
                self.scroll_down_day()  # اسکرول به سمت پایین برای افزایش روز
            else:
                self.scroll_up_day()  # اسکرول به سمت بالا برای کاهش روز

    def set_birth_date(self, year, month, day):
        """تنظیم تاریخ تولد کامل"""
        self.set_year(year)
        self.set_month(month)
        self.set_day(day)

    # همان متدهای scroll_up و scroll_down که قبلاً تعریف شدند
    def scroll_up_year(self):
        """اسکرول سال به سمت بالا"""
        year_picker = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/year"))
        )
        self.scroll_up(year_picker)

    def scroll_down_year(self):
        """اسکرول سال به سمت پایین"""
        year_picker = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/year"))
        )
        self.scroll_down(year_picker)

    # سایر متدهای scroll برای ماه و روز مشابه همین


class NotificationPermissionPage(BasePage):
    """کلاس مربوط به اجازه دسترسی به نوتیفیکیشن"""

    def allow_notification_permission(self):
        try:
            allow_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(
                    (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))
            )
            allow_button.click()
        except TimeoutException:
            # اگر صفحه مجوز نمایش داده نشود، ادامه دهید
            pass
