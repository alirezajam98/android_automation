import pytest
import allure
import json
from utils.config import configure_logger, capture_screenshot
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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


@allure.suite(f"version:{VERSION}")
@pytest.mark.order(1)
@allure.feature("Box Page")
@allure.story("Close Onboarding and Check Box Texts")
@allure.suite("Box Feature Tests")
@allure.severity(allure.severity_level.CRITICAL)
def test_close_onboarding_and_check_box_texts(login_and_dashboard):
    """تست بسته شدن انبوردینگ و بررسی متن‌های صفحه باکس"""

    box_page = login_and_dashboard
    driver = box_page.driver
    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()
    errors = []  # متغیری برای ذخیره خطاهای تست

    try:
        # مرحله 1: کلیک روی آیکون باکس برای باز کردن صفحه باکس
        with allure.step(f"Click on box icon to open box page for device"):
            logger.info(f"کلیک روی آیکون باکس برای باز کردن صفحه باکس: ")
            box_page = login_and_dashboard.click_box_icon()

        # مرحله 2: بستن صفحه انبوردینگ
        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            box_page.close_onboarding()

        # مرحله 3: بررسی نمایش صفحه باکس
        with allure.step("Check if the box page is displayed"):
            assert box_page.is_box_page_displayed(), "صفحه باکس بعد از بستن انبوردینگ نمایش داده نشده است."
            logger.info("بررسی نمایش صفحه باکس...")

        # مرحله 4: بررسی متن "۰ ریال" در صفحه باکس
        with allure.step("Check '۰ ریال' text"):
            try:
                expected_text = text_reference["box_page"]["box_deposit_text"]
                actual_text = box_page.get_box_deposit_text()
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن '۰ ریال' صحیح است: {actual_text}")
            except AssertionError as e:
                errors.append(f"Error in box_deposit_text: {e}")
                logger.error(str(e))

        # مرحله 5: بررسی متن "موجودی باکس‌ها"
        with allure.step("Check 'موجودی باکس‌ها' text"):
            try:
                expected_text = text_reference["box_page"]["box_deposit_description"]
                actual_text = box_page.get_box_deposit_description()
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن 'موجودی باکس‌ها' صحیح است: {actual_text}")
            except AssertionError as e:
                errors.append(f"Error in box_deposit_description: {e}")
                logger.error(str(e))

        # مرحله 6: بررسی متن "باکس فعالی ندارید"
        with allure.step("Check 'باکس فعالی ندارید' text"):
            try:
                expected_text = text_reference["box_page"]["no_active_box_title"]
                actual_text = box_page.get_no_active_box_title()
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن 'باکس فعالی ندارید' صحیح است: {actual_text}")
            except AssertionError as e:
                errors.append(f"Error in no_active_box_title: {e}")
                logger.error(str(e))

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        # گرفتن اسکرین‌شات در صورت بروز خطا
        screenshot_path = capture_screenshot(driver, "box_page_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e

    # بررسی خطاهای ثبت شده و پایان تست در صورت وجود خطا
    if errors:
        error_summary = "\n".join(errors)
        raise AssertionError(f"Errors encountered during test:\n{error_summary}")
    else:
        logger.info("تست بررسی متن‌های صفحه باکس با موفقیت انجام شد.")
