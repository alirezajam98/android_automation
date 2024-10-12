# tests/test_biometric_page.py
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService
from appium.options.common.base import AppiumOptions
from pages.login_page import LoginPage
from pages.biometric_page import BiometricPage
from pages.dashboard.dashboard_page import DashboardPage
from devices.device_config import device_configs
@pytest.fixture
def login_and_dashboard():
    options = AppiumOptions()
    options.load_capabilities(device_configs["Galaxy A11"])

    # ایجاد و راه‌اندازی سرویس Appium
    service = AppiumService()
    service.start()

    # بدست آوردن آدرس URL از سرویس (استفاده از پورت پیش‌فرض)
    appium_url = "http://127.0.0.1:4723"

    driver = webdriver.Remote(appium_url, options=options)

    # ورود به سیستم
    login_page = LoginPage(driver)
    login_page.enter_username("recap8")
    login_page.enter_password("Aa123456")

    # بعد از ورود، باید به صفحه بیومتریک هدایت شود
    biometric_page = login_page.click_login()

    # اکنون کاربر به صفحه Biometric هدایت می‌شود
    assert biometric_page.check_not_now(), "دکمه Not Now موجود نیست."

    # کلیک روی دکمه Not Now
    dashboard_page = biometric_page.click_not_now()
    # بررسی کنید که به صفحه داشبورد هدایت شده‌اید
    assert isinstance(dashboard_page, DashboardPage), "به صفحه Dashboard هدایت نشدید."
    assert dashboard_page.is_charge_button_displayed(), "دکمه شارژ در داشبورد نمایش داده نشده است."

    yield dashboard_page

    driver.quit()
    service.stop()