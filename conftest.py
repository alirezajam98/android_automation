# conftest.py
import pytest
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.login_page import LoginPage
from pages.dashboard.dashboard_page import DashboardPage
import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions
from devices.device_config import device_configs


@pytest.fixture(scope="function")
def setup(request):
    # گرفتن نام دستگاه و udid از آرگومان‌های command line
    device_name = request.config.getoption("--device_name")
    device_udid = request.config.getoption("--device_udid")

    # بارگذاری تنظیمات دستگاه
    options = AppiumOptions()
    options.load_capabilities(device_configs[device_name])

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--device_name", action="store", default="Galaxy A11", help="Device name for the tests")
    parser.addoption("--device_udid", action="store", default="", help="Device UDID")

@pytest.fixture
def device_name(request):
    return request.config.getoption("--device_name")

@pytest.fixture
def device_udid(request):
    return request.config.getoption("--device_udid")

@pytest.fixture
def login_and_dashboard():
    options = AppiumOptions()
    options.load_capabilities(device_configs["Galaxy A11"])

    # ایجاد و راه‌اندازی سرویس Appium
    service = AppiumService()
    service.start()

    appium_url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(appium_url, options=options)

    # ورود به سیستم
    login_page = LoginPage(driver)
    login_page.enter_username("andpfm7")
    login_page.enter_password("Aa123456")

    # هدایت به صفحه بیومتریک
    biometric_page = login_page.click_login()

    # صبر برای نمایش دکمه "Not Now" در صفحه بیومتریک
    not_now_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/btnNotNow")

    try:
        WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located(not_now_button)  # منتظر نمایش دکمه Not Now
        )
        biometric_page.click_not_now()
    except Exception as e:
        print(f"دکمه 'Not Now' در صفحه بیومتریک پیدا نشد: {e}")
        raise

    # هدایت به داشبورد
    dashboard_page = DashboardPage(driver)

    # بازگشت داشبورد برای استفاده در تست‌ها
    yield dashboard_page

    driver.quit()
    service.stop()


@pytest.fixture(scope="function")
def driver(request):
    # تنظیمات مورد نیاز برای Appium Driver
    desired_caps = {
        "platformName": "Android",
        "deviceName": request.config.getoption("--device_name"),
        "udid": request.config.getoption("--device_udid"),
        "appPackage": "com.samanpr.blu.dev",  # نام پکیج اپلیکیشن
        "appActivity": "com.samanpr.blu.MainActivity",  # اکتیویتی اصلی
        "automationName": "UiAutomator2",
        # تنظیمات دیگر بر حسب نیاز
    }

    # ساخت درایور
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    yield driver  # به تست داده می‌شود

    # بستن درایور بعد از اجرای تست‌ها
    driver.quit()