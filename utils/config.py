import json
import logging
import allure
import pytest
import yaml
import os

from datetime import datetime

from devices.device_config import device_configs


#
# def load_config():
#     # مسیر کامل به config.yml
#     config_path = 'C:\\Users\\a.jamshidi\\android_automation\\android_automation\\config.yml'
#     print(f"Loading config from: {config_path}")  # چاپ مسیر برای بررسی
#     with open(config_path, 'r') as file:
#         return yaml.safe_load(file)


# تنظیمات برای لاگ‌ها
def configure_logger():
    logger = logging.getLogger(__name__)
    if not logger.hasHandlers():
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            handlers=[logging.StreamHandler(), logging.FileHandler("test_log.log")]
        )
    return logger




# تنظیم لاگر
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logging.basicConfig(level=logging.INFO)
    logger.setLevel(logging.INFO)


# تابعی برای گرفتن اسکرین‌شات و افزودن به گزارش Allure
# def capture_screenshot(driver, step_name):
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     screenshot_name = f"{step_name}_{timestamp}.png"
#     screenshot_path = os.path.join("screenshots", screenshot_name)
#
#     # ایجاد پوشه screenshots در صورتی که وجود نداشته باشد
#     if not os.path.exists("screenshots"):
#         os.makedirs("screenshots")
#
#     driver.save_screenshot(screenshot_path)
#     with open(screenshot_path, "rb") as image_file:
#         allure.attach(image_file.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
#

def capture_screenshot(driver, name="screenshot"):
    # ایجاد پوشه `screenshots` در صورت عدم وجود
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    # ذخیره اسکرین‌شات در مسیر مشخص‌شده
    screenshot_path = os.path.join("screenshots", f"{name}.png")
    driver.save_screenshot(screenshot_path)
    return screenshot_path


# خواندن فایل JSON برای دریافت ترتیب تست‌ها
def load_test_order(file_path):
    if not os.path.exists(file_path):
        logger.error(f"Test order file '{file_path}' not found.")
        raise FileNotFoundError(f"Test order file '{file_path}' not found.")
    with open(file_path, "r") as file:
        return json.load(file)


def run_tests_for_device(device_name):
    # بارگذاری ترتیب تست‌ها از فایل
    test_order = load_test_order("test_order.json")

    # تنظیمات دستگاه انتخاب شده
    if device_name not in test_order["devices"]:
        logger.error(f"Device '{device_name}' not found in test order.")
        return

    device_config = device_configs.get(device_name, {})
    tests = test_order["devices"][device_name]

    # بررسی وجود تست‌ها برای دستگاه
    if not tests:
        logger.warning(f"No tests found for device '{device_name}'")
        return

    # ساخت لیستی از فایل‌های تست برای اجرا در یک pytest
    test_files = [
        test["file"] for test in tests
        if os.path.exists(test["file"]) and test.get("enabled", True)  # چک کردن 'enabled'
    ]

    if not test_files:
        logger.error(f"No valid test files found for device '{device_name}'")
        return

    # ایجاد پوشه 'report' اگر وجود ندارد
    report_dir = os.path.join(os.getcwd(), 'report')
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)

    # تنظیم مسیر گزارش نهایی برای هر دستگاه
    report_file = os.path.join(report_dir, f"report_{device_name}.html")

    pytest_args = [
        *test_files,  # لیست فایل‌های تست
        "-v",  # برای نمایش اطلاعات بیشتر
        f"--device_name={device_name}",
        f"--device_udid={device_config.get('udid', 'unknown_udid')}",  # تنظیم پیش‌فرض برای udid
        f"--html={report_file}",  # تولید گزارش HTML در مسیر جدید
        "--self-contained-html",  # ایجاد گزارش مستقل HTML
    ]
    pytest.main(pytest_args)
