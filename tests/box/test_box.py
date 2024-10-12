import pytest
import allure
from utils.config import configure_logger, capture_screenshot
import json

# تنظیمات لاگ
logger = configure_logger()

# تابعی برای بارگذاری فایل JSON
def load_text_reference():
    with open('text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@pytest.mark.order(1)
@pytest.mark.check_box
@allure.feature("Box Page")
@allure.story("Close Onboarding and Check Box Texts")
@allure.severity(allure.severity_level.CRITICAL)
def test_close_onboarding_and_check_box_texts(login_and_dashboard, device_name):
    """تست بسته شدن انبوردینگ و بررسی متن‌های صفحه باکس"""

    box_page = login_and_dashboard
    driver = box_page.driver

    # بارگذاری فایل JSON برای دریافت متون مرجع
    text_reference = load_text_reference()

    # متغیر برای ذخیره نتیجه تست
    errors = []

    try:
        with allure.step(f"Click on box icon to open box page for device: {device_name}"):
            logger.info(f"کلیک روی آیکون باکس برای باز کردن صفحه باکس: {device_name}")
            box_page = login_and_dashboard.click_box_icon()

        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            box_page.close_onboarding()

        with allure.step("Check if the box page is displayed"):
            assert box_page.is_box_page_displayed(), "صفحه باکس بعد از بستن انبوردینگ نمایش داده نشده است."
            logger.info("بررسی نمایش صفحه باکس...")

        # مقایسه مقادیر با متون مرجع از فایل JSON
        with allure.step("Check '۰ ریال' text"):
            try:
                expected_text = text_reference["box_page"]["box_deposit_text"]
                actual_text = box_page.get_box_deposit_text()  # تابعی که متن واقعی را برمی‌گرداند
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"بررسی متن '{expected_text}' پاس شد.")
            except AssertionError as e:
                errors.append(f"Error in box_deposit_text: {e}")
                logger.error(str(e))

        with allure.step("Check 'موجودی باکس‌ها' text"):
            try:
                expected_text = text_reference["box_page"]["box_deposit_description"]
                actual_text = box_page.get_box_deposit_description()  # تابعی که متن واقعی را برمی‌گرداند
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"بررسی متن '{expected_text}' پاس شد.")
            except AssertionError as e:
                errors.append(f"Error in box_deposit_description: {e}")
                logger.error(str(e))

        with allure.step("Check 'باکس فعالی ندارید' text"):
            try:
                expected_text = text_reference["box_page"]["no_active_box_title"]
                actual_text = box_page.get_no_active_box_title()  # تابعی که متن واقعی را برمی‌گرداند
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"بررسی متن '{expected_text}' پاس شد.")
            except AssertionError as e:
                errors.append(f"Error in no_active_box_title: {e}")
                logger.error(str(e))

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "box_page_error")
        raise e

    # گزارش خطاهای ثبت شده (در صورت وجود)
    if errors:
        raise AssertionError("Errors encountered during test:\n" + "\n".join(errors))

    logger.info("تمام متن های باکس پاس شده‌اند.")
