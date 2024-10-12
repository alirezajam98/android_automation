import os
import pytest
import allure
from logging_config import logger
from datetime import datetime


# تابعی برای گرفتن اسکرین‌شات و اتصال آن به گزارش Allure
def capture_screenshot(driver, step_name):
    try:
        # اضافه کردن timestamp برای نام فایل
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_name = f"{step_name}_{timestamp}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)

        # اطمینان از وجود پوشه‌ی screenshots
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # گرفتن اسکرین‌شات
        driver.save_screenshot(screenshot_path)

        # افزودن اسکرین‌شات به گزارش Allure
        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
    except Exception as e:
        logger.error(f"Failed to capture screenshot: {e}")


@pytest.mark.order(0)  # ترتیب اجرای تست
@allure.feature("Login")  # ویژگی اصلی برای لاگین
@allure.story("Login and Navigate to Settings")  # داستانی که تست را توصیف می‌کند
@allure.severity(allure.severity_level.CRITICAL)  # سطح اهمیت تست
def test_login_and_go_to_settings(login_and_dashboard):
    """تست لاگین و ورود به صفحه تنظیمات از داشبورد"""

    dashboard_page = login_and_dashboard
    driver = dashboard_page.driver  # فرض می‌کنیم driver در اینجا وجود دارد

    try:
        with allure.step("Start test: open profile page from dashboard"):
            logger.info("Starting test open profile page...")

        with allure.step("Click on settings button in the dashboard"):
            logger.info("کلیک روی دکمه تنظیمات در داشبورد...")
            settings_page = dashboard_page.click_settings_button()

        with allure.step("Check if the settings page is displayed"):
            assert settings_page.is_page_displayed(), "صفحه تنظیمات نمایش داده نشده است."
            allure.attach("Settings Page", "Settings page displayed successfully", allure.attachment_type.TEXT)
            logger.info("وارد صفحه تنظیمات شدید.")

    except AssertionError as e:
        # در صورت بروز خطا، اسکرین‌شات گرفته و به گزارش اضافه می‌شود
        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "settings_page_error")
        raise e  # بالا بردن مجدد خطا برای ثبت در pytest

    except Exception as e:
        # برای هر خطای غیرمنتظره، اسکرین‌شات گرفته می‌شود
        logger.error(f"Unexpected error: {e}")
        capture_screenshot(driver, "unexpected_error")
        raise e

    logger.info("Test completed successfully.")
    allure.attach("Test Result", "Test completed successfully", allure.attachment_type.TEXT)
