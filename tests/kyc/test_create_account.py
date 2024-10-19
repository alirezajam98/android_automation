import pytest
import allure
from appium.options.common import AppiumOptions
from appium.webdriver import webdriver
from appium.webdriver.appium_service import AppiumService
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy

from devices.device_config import device_configs
from utils.config import configure_logger, capture_screenshot  # تنظیمات لاگ و تابع اسکرین‌شات

# تنظیمات لاگ
logger = configure_logger()


@pytest.mark.order(1)  # اولویت تست
@allure.feature("User Account Creation")  # ویژگی
@allure.story("Create a new user account")  # داستان تست
@allure.severity(allure.severity_level.CRITICAL)  # سطح اهمیت
@pytest.mark.order(1)
def test_kyc(open_app_without_login):
    driver = open_app_without_login

    try:
        # مرحله 1: کلیک روی دکمه 'ایجاد حساب کاربری'
        with allure.step("Click on 'Create Account' button"):
            logger.info("کلیک روی دکمه 'ایجاد حساب کاربری'...")
            create_account_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
            )
            create_account_button.click()
            logger.info("دکمه 'ایجاد حساب کاربری' کلیک شد.")
            # بررسی دسترسی نوتیفیکیشن (Allow)
            try:
                allow_button = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
                WebDriverWait(driver, 5).until(
                    EC.visibility_of_element_located(allow_button)
                )
                driver.find_element(*allow_button).click()
                logger.info("Clicked on 'Allow' button for notification permission.")
            except TimeoutException:
                logger.info("No notification permission modal displayed, continuing.")

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
