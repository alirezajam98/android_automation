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


class BirthDatePage(BasePage):

    def scroll_year(self):
        """اسکرول کردن سال با استفاده از ActionChains با مختصات مطلق"""
        actions = ActionChains(self.driver)
        # استفاده از مختصات مطلق
        actions.w3c_actions.pointer_action.move_to_location(231, 2279)  # حرکت به موقعیت شروع به صورت مطلق
        actions.w3c_actions.pointer_action.pointer_down()  # شروع حرکت
        actions.w3c_actions.pointer_action.move_to_location(231, 2747)  # حرکت به موقعیت پایان به صورت مطلق
        actions.w3c_actions.pointer_action.release()  # رها کردن کلیک
        actions.perform()

    def click_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/nextButton"))
        )
        next_button.click()


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
