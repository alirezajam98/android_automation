import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from utils.config import configure_logger, capture_screenshot  # تنظیمات لاگ و تابع اسکرین‌شات

# تنظیمات لاگ
logger = configure_logger()


@pytest.mark.order(1)  # اولویت تست
@allure.feature("User Account Creation")  # ویژگی
@allure.story("Create a new user account")  # داستان تست
@allure.severity(allure.severity_level.CRITICAL)  # سطح اهمیت
def test_create_account(login_and_dashboard):
    """تست ایجاد حساب کاربری جدید"""

    # صفحه داشبورد (یا صفحه ورود اولیه)
    dashboard_page = login_and_dashboard
    driver = dashboard_page.driver

    try:
        # مرحله 1: کلیک روی دکمه 'ایجاد حساب کاربری'
        with allure.step("Click on 'Create Account' button"):
            logger.info("کلیک روی دکمه 'ایجاد حساب کاربری'...")
            create_account_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
            )
            create_account_button.click()
            logger.info("دکمه 'ایجاد حساب کاربری' کلیک شد.")

        # مرحله 2: کلیک روی دکمه 'بازکردن حساب'
        with allure.step("Click on 'Open Account' button"):
            logger.info("کلیک روی دکمه 'بازکردن حساب'...")
            open_account_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openAccountButton"))
            )
            open_account_button.click()
            logger.info("دکمه 'بازکردن حساب' کلیک شد.")

        # مرحله 3: انتخاب UAT در سرور
        with allure.step("Select 'UAT' from server selection"):
            logger.info("انتخاب سرور 'UAT'...")
            uat_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                                'new UiSelector().className("android.view.ViewGroup").instance(3)'))
            )
            uat_button.click()
            logger.info("سرور 'UAT' انتخاب شد.")

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "account_creation_error")
        raise e
