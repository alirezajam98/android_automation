#############################احرای تکی روی گوشی ها ###################################
import json
import os
import pytest
import logging
from devices.device_config import device_configs  # برای بارگذاری تنظیمات دستگاه‌ها

# تنظیم لاگر
logger = logging.getLogger(__name__)
if not logger.hasHandlers():
    logging.basicConfig(level=logging.INFO)
    logger.setLevel(logging.INFO)


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


if __name__ == "__main__":
    devices = ["Galaxy S24 Ultra"]  # لیست دستگاه‌ها
    for device in devices:
        logger.info(f"Running tests on {device}...")
        run_tests_for_device(device)
################################اجرای تست‌ها به‌صورت موازی (Parallel)######################################
#
# import json
# import os
# import pytest
# import logging
# from multiprocessing import Process
# from devices.device_config import device_configs  # برای بارگذاری تنظیمات دستگاه‌ها
#
# # تنظیم لاگر
# logger = logging.getLogger(__name__)
# if not logger.hasHandlers():
#     logging.basicConfig(level=logging.INFO)
#     logger.setLevel(logging.INFO)
#
#
# # خواندن فایل JSON برای دریافت ترتیب تست‌ها
# def load_test_order(file_path):
#     if not os.path.exists(file_path):
#         logger.error(f"Test order file '{file_path}' not found.")
#         raise FileNotFoundError(f"Test order file '{file_path}' not found.")
#     with open(file_path, "r") as file:
#         return json.load(file)
#
#
# def run_tests_for_device(device_name):
#     # بارگذاری ترتیب تست‌ها از فایل
#     test_order = load_test_order("test_order.json")
#
#     # تنظیمات دستگاه انتخاب شده
#     if device_name not in test_order["devices"]:
#         logger.error(f"Device '{device_name}' not found in test order.")
#         return
#
#     device_config = device_configs.get(device_name, {})
#     tests = test_order["devices"][device_name]
#
#     # بررسی وجود تست‌ها برای دستگاه
#     if not tests:
#         logger.warning(f"No tests found for device '{device_name}'")
#         return
#
#     # ساخت لیستی از فایل‌های تست برای اجرا در یک pytest
#     test_files = [test["file"] for test in tests if os.path.exists(test["file"])]
#
#     if not test_files:
#         logger.error(f"No valid test files found for device '{device_name}'")
#         return
#
#     # ارسال پارامترهای دستگاه به pytest و اجرای همه تست‌ها یکجا
#     report_file = f"report_{device_name}.html"  # گزارش نهایی برای هر دستگاه
#
#     pytest_args = [
#         *test_files,  # لیست فایل‌های تست
#         "-v",  # برای نمایش اطلاعات بیشتر
#         f"--device_name={device_name}",
#         f"--device_udid={device_config.get('udid', 'unknown_udid')}",  # تنظیم پیش‌فرض برای udid
#         f"--html={report_file}",  # تولید گزارش HTML
#         "--self-contained-html",  # ایجاد گزارش مستقل HTML
#         "-n", "1",  # اجرای تست‌ها به‌صورت موازی با یک پروسه جدا برای هر دستگاه
#     ]
#     pytest.main(pytest_args)
#
#
# if __name__ == "__main__":
#     devices = ["Galaxy A11", "Galaxy A7"]  # لیست دستگاه‌ها
#     processes = []
#
#     # ایجاد پروسه جداگانه برای هر دستگاه
#     for device in devices:
#         p = Process(target=run_tests_for_device, args=(device,))
#         processes.append(p)
#         p.start()
#
#     # منتظر ماندن برای اتمام همه پروسه‌ها
#     for p in processes:
#         p.join()
