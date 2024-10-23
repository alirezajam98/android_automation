import random

import pytest
from appium.webdriver.appium_service import AppiumService
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from appium.options.common.base import AppiumOptions
from devices.device_config import device_configs
import logging

# تنظیم لاگر برای نمایش فقط لاگ‌های INFO و ERROR
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # فقط پیام‌های INFO و بالاتر نمایش داده می‌شود

from pages.dashboard.dashboard_page import DashboardPage


@pytest.fixture(scope="function")
def setup(request):
    device_name = request.config.getoption("--device_name")
    device_udid = request.config.getoption("--device_udid")

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
def open_app_without_login(request):
    device_name = request.config.getoption("--device_name")
    options = AppiumOptions()
    options.load_capabilities(device_configs[device_name])

    service = AppiumService()
    service.start()

    appium_url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(appium_url, options=options)

    # باز کردن اپ بدون لاگین
    logger.info("App opened without logging in.")

    yield driver

    driver.quit()
    service.stop()


@pytest.fixture
def login_and_dashboard(request):
    from pages.login_page import LoginPage
    device_name = request.config.getoption("--device_name")
    options = AppiumOptions()
    options.load_capabilities(device_configs[device_name])

    service = AppiumService()
    service.start()

    appium_url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(appium_url, options=options)
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
    # ورود به سیستم
    login_page = LoginPage(driver)
    login_page.enter_username("andpfm7")
    login_page.enter_password("Aa123456")

    biometric_page = login_page.click_login()

    # بستن صفحه بیومتریک (در صورت نمایش)
    not_now_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/btnNotNow")
    try:
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(not_now_button)
        )

        biometric_page.click_not_now()
        logger.info("Clicked on 'Not Now' button in biometric page.")
    except TimeoutException:
        logger.info("No biometric page displayed, skipping.")

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

    # هدایت به داشبورد
    dashboard_page = DashboardPage(driver)
    try:
        dashboard_identifier = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(dashboard_identifier)
        )
        logger.info("Dashboard page displayed successfully.")
    except TimeoutException:
        logger.error("Failed to load the dashboard page.")

    yield dashboard_page

    driver.quit()
    service.stop()


@pytest.fixture(scope="function")
def driver(request):
    device_name = request.config.getoption("--device_name")
    device_udid = request.config.getoption("--device_udid")

    desired_caps = {
        "platformName": device_configs[device_name]["platformName"],
        "deviceName": device_name,
        "udid": device_udid,
        "appPackage": device_configs[device_name]["appPackage"],
        "appActivity": device_configs[device_name]["appActivity"],
        "automationName": device_configs[device_name]["automationName"]
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()


def mobile_number_generator():
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    mobile_number = "091" + random_digits
    return mobile_number


# مثال استفاده از تابع


def national_code_generator():
    number_list = []
    sum_digits = 0

    # ایجاد ارقام تصادفی و محاسبه‌ی جمع ضرب‌ها
    for i in range(10, 1, -1):
        j = random.randint(0, 9)
        number_list.append(j)
        sum_digits += j * i

    # محاسبه‌ی رقم کنترل
    m = sum_digits % 11
    if m < 2:
        number_list.append(m)
    else:
        number_list.append(11 - m)

    # ترکیب لیست ارقام به یک رشته
    national_code = ''.join(map(str, number_list))

    return national_code


import os


# تابع برای خواندن شمارنده از فایل
def read_counter(filename='utils/counter.txt'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return int(file.read().strip())  # خواندن و برگرداندن مقدار شمارنده
    return 1  # اگر فایل وجود ندارد، شمارنده را با 1 شروع می‌کنیم


# تابع برای نوشتن شمارنده در فایل
def write_counter(counter, filename='utils/counter.txt'):
    with open(filename, 'w') as file:
        file.write(str(counter))  # ذخیره شمارنده در فایل


# تابع تولید یوزرنیم با استفاده از شمارنده
def username_generator():
    # خواندن شمارنده از فایل
    counter = read_counter()

    # تولید یوزرنیم با استفاده از شمارنده
    username = f"ajcard{counter}"

    # افزایش شمارنده و ذخیره آن در فایل
    counter += 1
    write_counter(counter)

    return username


# تست تولید یوزرنیم
new_username = username_generator()
print(new_username)
print(
    national_code_generator()
)