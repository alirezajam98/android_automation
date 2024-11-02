import json
from time import sleep
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import mobile_number_generator, national_code_generator, username_generator
from pages.kyc.kyc_pages import NotificationPermissionPage, OpenAccountPage, SelectServerPage, \
    CreateAccountInfoPage, AcceptRulesAndRegulations, EnterPhoneNumberPage, ReferralPage, NationalCodePage, \
    BirthDatePage, UserNamePage, PasswordPage, CreateAccountInBluStatePage, SelectNationalCardOrTrackerIdPage, \
    TakePhotoPage, ConfirmPhotoPage, ConfirmPhotoModal, SelectJobPage, VideoDemoPage, \
    VideoRecordingPage, ConfirmVideoModal, FinalPage
from pages.login_page import LoginPage
from utils.common_flows import setup_user_account_creation_steps
from utils.config import configure_logger, capture_screenshot  # تنظیمات لاگ و تابع اسکرین‌شات

# تنظیمات لاگ
logger = configure_logger()


# تابعی برای بارگذاری فایل JSON
def load_text_reference():
    with open('utils/text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)


# بارگذاری نسخه از فایل
with open('utils/version.json') as f:
    config = json.load(f)
    VERSION = config.get("version", "unknown_version")  # مقدار پیش‌فرض در صورت نبود نسخه


@allure.epic("KYC")
@allure.feature("Create a new user account_National_ID_upload")
# @allure.story("Create a new user account_National_ID_upload")
@allure.suite(f"version:{VERSION}")
@allure.sub_suite("Tests for Create account by ID card")
@allure.severity(allure.severity_level.BLOCKER)
def test_national_id_card_upload(open_app_without_login):
    driver = open_app_without_login
    # تولید داده‌های کاربر
    phone_number = mobile_number_generator()
    national_code = national_code_generator()
    username = username_generator()
    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()

    # اجرای مراحل مشترک
    setup_user_account_creation_steps(driver, phone_number, national_code, username, text_reference)
    try:
        # مرحله 17: انتخاب گزینه 'کارت ملی'
        with allure.step("Select 'National Card' option"):
            select_national_card = SelectNationalCardOrTrackerIdPage(driver)
            select_national_card.click_select_national_card()
            logger.info("گزینه 'کارت ملی' انتخاب شد.")

        try:
            camera_permission_page = NotificationPermissionPage(driver)
            camera_permission_page.allow_camera_permission()
            logger.info("دسترسی به دوربین تأیید شد.")
        except TimeoutException:
            logger.info("مجوز دوربین نمایش داده نشد، ادامه دهید.")

        # مرحله 18: گرفتن عکس جلو و پشت کارت ملی
        with allure.step("Take photo from front of national card"):
            take_photo_page = TakePhotoPage(driver)
            take_photo_page.click_take_photo()
            logger.info("عکس جلوی کارت ملی گرفته شد.")

        with allure.step("Click confirm button"):
            confirm_photo_page = ConfirmPhotoPage(driver)
            confirm_photo_page.click_confirm_photo()
            confirm_photo_modal = ConfirmPhotoModal(driver)
            confirm_photo_modal.click_confirm_photo()
            logger.info("عکس تایید شد.")

        with allure.step("Take photo from back of national card"):
            take_photo_page.click_take_photo()
            logger.info("عکس پشت کارت ملی گرفته شد.")

        with allure.step("Click confirm button"):
            confirm_photo_page.click_confirm_photo()
            confirm_photo_modal.click_confirm_photo()
            logger.info("عکس تایید شد.")

        with allure.step("Click next button"):
            logger.info("کلیک روی دکمه 'ادامه'...")
            create_account_in_blu_state_page = CreateAccountInBluStatePage(driver)
            create_account_in_blu_state_page.click_confirm_button()
            logger.info("دکمه 'ادامه' کلیک شد.")

        # مرحله 19: انتخاب شغل
        with allure.step("Select job for user"):
            logger.info("کلیک بر روی اولین شغل")
            select_job_page = SelectJobPage(driver)
            select_job_page.select_job()
            logger.info("اولین شغل از لیست انتخاب شد.")
            logger.info("کلیک روی دکمه تایید...")
            select_job_page.click_confirm_job()
            logger.info("دکمه 'ادامه' کلیک شد.")

        with allure.step("Show and skip demo video"):
            logger.info("ویدیو آموزشی در حال پخش است ...")
            video_demo_page = VideoDemoPage(driver)
            video_demo_page.click_confirm_video_demo()
            logger.info("ویدیو آموزشی پخش و بر روی ادامه کلیک شد.")

        try:
            camera_permission_page.allow_camera_permission()
            logger.info("مجوز دوربین تأیید شد.")
        except TimeoutException:
            logger.info("مجوز دوربین نمایش داده نشد.")

        # مرحله 21: ضبط ویدیو
        with allure.step("Record video"):
            logger.info("دوربین سلفی جهت فیلم برداری باز شد...")
            video_record_page = VideoRecordingPage(driver)
            video_record_page.click_video_recording()
            logger.info("ضبط ویدیو شروع شد.")
            sleep(10)
            video_record_page.click_stop_recording_button()
            logger.info("ضبط ویدیو متوقف شد.")
            video_record_page.click_upload_video()
            logger.info("ویدیو آپلود شد.")

        with allure.step("Confirm video upload"):
            confirm_video_modal = ConfirmVideoModal(driver)
            confirm_video_modal.click_confirm_video()
            logger.info("آپلود ویدیو تایید شد.")

        # مرحله 22: تایید نهایی و پایان
        with allure.step("Final confirmation"):
            final_page = FinalPage(driver)
            final_page.click_final_confirm()
            logger.info("مراحل ایجاد حساب کاربری با موفقیت به پایان رسید.")

        # مرحله 23: ورود به صفحه ورود و مقایسه نام کاربری
        with allure.step("Verify displayed username in login page"):
            logger.info("انتقال به صفحه ورود و بررسی نام کاربری...")
            login_page = LoginPage(driver)

            # گرفتن متن از فیلد نام کاربری در صفحه ورود
            displayed_username = login_page.get_username_text()

            # مقایسه با نام کاربری تولید شده در ابتدا
            assert displayed_username == username, f"Mismatch in username: Expected '{username}', but got '{displayed_username}'"
            logger.info(f"Username verification successful: {displayed_username}")
    except Exception as e:

        logger.error(f"خطا رخ داد: {e}")
        # اسکرین‌شات در صورت بروز هرگونه خطا
        screenshot_path = capture_screenshot(driver, "account_creation_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
