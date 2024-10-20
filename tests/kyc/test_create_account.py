import json
import time
from time import sleep

import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import mobile_number_generator, national_code_generator
from pages.kyc.kyc_pages import NotificationPermissionPage, CreateAccountPage, OpenAccountPage, SelectServerPage, \
    CreateAccountInfoPage, AcceptRulesAndRegulations, EnterPhoneNumberPage, ReferralPage, NationalCodePage, \
    BirthDatePage
from utils.config import configure_logger, capture_screenshot  # تنظیمات لاگ و تابع اسکرین‌شات

# تنظیمات لاگ
logger = configure_logger()


# تابعی برای بارگذاری فایل JSON
def load_text_reference():
    with open('text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)


@pytest.mark.order(1)
@allure.feature("User Account Creation")
@allure.story("Create a new user account")
@allure.severity(allure.severity_level.CRITICAL)
def test_kyc(open_app_without_login):
    driver = open_app_without_login
    accept_page = AcceptRulesAndRegulations(driver)
    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()

    # متغیر برای ذخیره نتیجه تست
    errors = []
    try:
        # بررسی دسترسی نوتیفیکیشن
        notification_permission_page = NotificationPermissionPage(driver)
        notification_permission_page.allow_notification_permission()
        logger.info("Clicked on 'Allow' button for notification permission.")

        # مرحله 1: کلیک روی دکمه 'ایجاد حساب کاربری'
        try:
            with allure.step("Click on 'Create Account' button"):
                logger.info("کلیک روی دکمه 'ایجاد حساب کاربری'...")
                create_account_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
                )
                create_account_button.click()
                logger.info("دکمه 'ایجاد حساب کاربری' کلیک شد.")
        except TimeoutException:
            logger.info("No login page displayed, continuing.")

        # مرحله 2: کلیک روی دکمه 'بازکردن حساب'
        with allure.step("Click on 'Open Account' button"):
            logger.info("کلیک روی دکمه 'بازکردن حساب'...")
            open_account_page = OpenAccountPage(driver)
            open_account_page.click_open_account()
            logger.info("دکمه 'بازکردن حساب' کلیک شد.")

        # مرحله 3: انتخاب UAT در سرور
        with allure.step("click on 'UAT' from server selection"):
            logger.info("انتخاب سرور 'UAT'...")
            select_server_page = SelectServerPage(driver)
            select_server_page.select_uat_server()
            logger.info("سرور 'UAT' انتخاب شد.")

        # مرحله 4: کلیک روی 'شروع'
        with allure.step("Click on 'Start' button"):
            logger.info("کلیک روی دکمه 'شروع'...")
            create_account_info_page = CreateAccountInfoPage(driver)
            create_account_info_page.click_start()
            logger.info("دکمه 'شروع' کلیک شد.")

        # بررسی وضعیت اولیه سوییچ
        with allure.step("Check initial state of the switch"):
            initial_status = accept_page.is_switch_on()
            logger.info(f"Initial switch status: {'ON' if initial_status else 'OFF'}")
            allure.attach(f"Initial switch status: {'ON' if initial_status else 'OFF'}", "Switch Status",
                          allure.attachment_type.TEXT)

        # تغییر وضعیت سوییچ
        with allure.step("Toggle the agreement switch"):
            logger.info("کلیک بر روی تاگل سوییچ موافقت با قوانین و مقررات ...")
            accept_page.toggle_switch()  # استفاده از متد toggle_switch
            new_status = accept_page.is_switch_on()
            logger.info(f"Switch status after toggle: {'ON' if new_status else 'OFF'}")
            allure.attach(f"New switch status: {'ON' if new_status else 'OFF'}", "Switch Status After Toggle",
                          allure.attachment_type.TEXT)

        # کلیک روی دکمه تایید بعد از تغییر وضعیت
        with allure.step("Click confirm button after toggle"):
            logger.info("کلیک روی دکمه تایید...")
            accept_page.click_confirm_button()
            logger.info("دکمه تایید کلیک شد و به صفحه وارد کردن شماره تلفن هدایت شد.")
        # مرحله 2: وارد کردن شماره تلفن
        with allure.step("Enter phone number"):
            logger.info("ورود شماره تلفن ...")
            # فراخوانی تابع mobile_number_generator برای تولید شماره موبایل
            phone_number = mobile_number_generator()
            phone_page = EnterPhoneNumberPage(driver)
            phone_page.enter_phone_number(phone_number)

        logger.info(f"شماره تلفن وارد شد: {phone_number}")

        # مرحله 3: کلیک روی دکمه "بعدی"
        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'بعدی'...")
            phone_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        with (allure.step("Click next button")):
            logger.info("کلیک روی دکمه 'بعدی'...")
            referral_page = ReferralPage(driver)
            referral_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        # بررسی متن کد ملی
        with allure.step("Check 'کد ملی ۱۰ رقمی' text"):
            logger.info("بررسی متن کد ملی...")
            expected_text = text_reference["kyc_pages"]["national_code"]

            # استفاده از شیء درست برای فراخوانی متد
            national_page = NationalCodePage(driver)
            actual_text = national_page.get_national_code_text()  # به درستی شیء phone_page استفاده می‌شود

            assert actual_text == expected_text, \
                f"Expected '{expected_text}', but got '{actual_text}'"
            logger.info(f"متن کد ملی صحیح است: {actual_text}")

        with allure.step("Enter national code"):
            logger.info("ورود کد ملی ...")

            try:
                # فراخوانی تابع national_code_generator برای تولید کد ملی
                national_code = national_code_generator()
                national_code_page = NationalCodePage(driver)

                # افزایش زمان انتظار به 20 ثانیه
                national_code_page.enter_national_code(national_code)
                logger.info(f"کدملی وارد شد: {national_code}")

            except TimeoutException as e:
                logger.error(f"خطا در پیدا کردن فیلد کد ملی: {e}")
                capture_screenshot(driver, "national_code_error")
                raise e

        # مرحله 3: کلیک روی دکمه "بعدی"
        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'بعدی'...")
            national_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        with allure.step("Scroll year field"):
            birth_date_page = BirthDatePage(driver)
            birth_date_page.scroll_year()  # اسکرول کردن سال
            logger.info("سال با موفقیت اسکرول شد.")

        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'بعدی'...")
            birth_date_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")


    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "account_creation_error")
        raise e
