import json
import time
from time import sleep

import pytest
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conftest import mobile_number_generator, national_code_generator, username_generator
from pages.kyc.kyc_pages import NotificationPermissionPage, CreateAccountPage, OpenAccountPage, SelectServerPage, \
    CreateAccountInfoPage, AcceptRulesAndRegulations, EnterPhoneNumberPage, ReferralPage, NationalCodePage, \
    BirthDatePage, UserNamePage, PasswordPage, CreateAccountInBluStatePage, SelectNationalCardOrTrackerIdPage, \
    TakePhotoPage, ConfirmPhotoPage, ConfirmPhotoModal, UploadPhotoModal, SelectJobPage, VideoDemoPage, \
    VideoRecordingPage, ConfirmVideoModal, FinalPage
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
        try:
            notification_permission_page = NotificationPermissionPage(driver)
            notification_permission_page.allow_notification_permission()
            logger.info("Clicked on 'Allow' button for notification permission.")
        except TimeoutException:
            logger.info("No notification permission modal displayed, continuing.")
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

        with allure.step("Check 'مانند:‌ MDMGKP' text"):
            logger.info("بررسی متن ریفرال...")
            expected_text = text_reference["kyc_pages"]["referralInputEditText"]

            # استفاده از شیء درست برای فراخوانی متد
            referral_page = ReferralPage(driver)
            actual_text = referral_page.get_referral_field_text()  # به درستی شیء ReferralPage استفاده می‌شود

            assert actual_text == expected_text, \
                f"Expected '{expected_text}', but got '{actual_text}'"
            logger.info(f"متن ریفرال صحیح است: {actual_text}")

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
            actual_text = national_page.get_national_code_text()  # به درستی شیء national_page استفاده می‌شود

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

        with allure.step("write new username"):
            logger.info("وارد کردن نام کاربری ...")
            try:
                # فراخوانی تابع username_generator برای تولید کد ملی
                username = username_generator()
                username_page = UserNamePage(driver)
                username_page.enter_username(username)
                logger.info(f"نام کاربری وارد شد: {username}")

            except TimeoutException as e:
                logger.error(f"خطا در پیدا کردن فیلد نام کاربری: {e}")
                capture_screenshot(driver, "username_field_error")
                raise e

        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'بعدی'...")
            username_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        with allure.step("Enter password"):
            logger.info("وارد کردن رمز عبور")
            password_page = PasswordPage(driver)
            password_page.enter_password("Aa123456")
            logger.info("رمز عبور وارد شد.")

        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'بعدی'...")
            password_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'ادامه'...")
            create_account_in_blu_state_page = CreateAccountInBluStatePage(driver)
            create_account_in_blu_state_page.click_confirm_button()
            logger.info("دکمه 'ادامه' کلیک شد.")

        with allure.step("select national card button"):
            logger.info("کلیک روی دکمه 'ساخت اکانت با کارت ملی'...")
            select_national_card = SelectNationalCardOrTrackerIdPage(driver)
            select_national_card.click_select_national_card()
            logger.info("دکمه 'ساخت اکانت با کارت ملی' کلیک شد.")

        try:
            camera_permission_page = NotificationPermissionPage(driver)
            camera_permission_page.allow_camera_permission()
            logger.info("Clicked on 'Allow' button for camera permission.")
        except TimeoutException:
            logger.info("No notification permission modal displayed, continuing.")

        with allure.step("Take photo from front of nationalcard"):
            logger.info("کلیک بر روی دکمه شاتر برای 'عکس جلوی کارت ملی'...")
            take_photo_page = TakePhotoPage(driver)
            take_photo_page.click_take_photo()
            logger.info("دکمه شاتر برای عکس برداری کلیک شد.")

        with allure.step("Click confirm button"):
            logger.info("کلیک روی دکمه تایید...")
            confirm_photo_page = ConfirmPhotoPage(driver)
            confirm_photo_page.click_confirm_photo()
            logger.info("دکمه تایید کلیک شد.")

        with allure.step("Click confirm button"):
            logger.info("کلیک روی دکمه تایید...")
            confirm_photo_modal = ConfirmPhotoModal(driver)
            confirm_photo_modal.click_confirm_photo()
            logger.info("دکمه تایید کلیک شد.")

        with allure.step("Take photo from back of nationalcard"):
            logger.info("کلیک بر روی دکمه شاتر برای 'عکس پشت کارت ملی'...")
            take_photo_page = TakePhotoPage(driver)
            take_photo_page.click_take_photo()
            logger.info("دکمه شاتر برای عکس برداری کلیک شد.")

        with allure.step("Click confirm button for back card"):
            logger.info("کلیک روی دکمه تایید...")
            confirm_photo_page = ConfirmPhotoPage(driver)
            confirm_photo_page.click_confirm_photo()
            logger.info("دکمه تایید کلیک شد.")

        with allure.step("Click confirm button"):
            logger.info("کلیک روی دکمه تایید...")
            confirm_photo_modal = ConfirmPhotoModal(driver)
            confirm_photo_modal.click_confirm_photo()
            logger.info("دکمه تایید کلیک شد.")

        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'ادامه'...")
            create_account_in_blu_state_page = CreateAccountInBluStatePage(driver)
            create_account_in_blu_state_page.click_confirm_button()
            logger.info("دکمه 'ادامه' کلیک شد.")

        with allure.step("Select job for user"):
            logger.info("کلیک بر روی اولین شغل")
            select_job_page = SelectJobPage(driver)
            select_job_page.select_job()
            logger.info("اولین شغل از لیست انتخاب شد.")
            logger.info("کلیک روی دکمه تایید...")
            select_job_page.click_confirm_job()
            logger.info("دکمه 'ادامه' کلیک شد.")

        with allure.step("show and skip demo video"):
            logger.info("ویدیو آموزشی نحوه ارسال ویدیو در حال پخش است...")
            video_demo_page = VideoDemoPage(driver)
            video_demo_page.click_confirm_video_demo()
            logger.info("دکمه 'ادامه' کلیک شد.")

        try:
            camera_permission_page = NotificationPermissionPage(driver)
            camera_permission_page.allow_camera_permission()
            logger.info("Clicked on 'Allow' button for camera permission.")
        except TimeoutException:
            logger.info("No notification permission modal displayed, continuing.")

        with allure.step("record video"):
            logger.info("کلیک روی دکمه ریکورد ویدیو")
            video_record_page = VideoRecordingPage(driver)
            video_record_page.click_video_recording()
            logger.info("ویدیو در حال ضبط شدن است...")
            sleep(10)
            video_record_page.click_stop_recording_button()
            logger.info("توقف ضبط ویدیو.")
            logger.info("کلیک روی آپلود ویدیو")
            video_record_page.click_upload_video()
            logger.info("ویدیو در حال آپلود است...")
            confirm_video_modal = ConfirmVideoModal(driver)
            confirm_video_modal.click_confirm_video()
            logger.info("کلیک روی تایید آپلود ویدیو")
            final_page = FinalPage(driver)
            final_page.click_final_confirm()
            logger.info("مراحل ایجاد حساب کاربری با موفقیت به پایان رسید")

    except Exception as e:

        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "account_creation_error")
        raise e
