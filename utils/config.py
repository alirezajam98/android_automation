import logging
import allure
import yaml
import os
from datetime import datetime


def load_config():
    # مسیر کامل به config.yml
    config_path = 'C:\\Users\\a.jamshidi\\android_automation\\android_automation\\config.yml'
    print(f"Loading config from: {config_path}")  # چاپ مسیر برای بررسی
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


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


# تابعی برای گرفتن اسکرین‌شات و افزودن به گزارش Allure
def capture_screenshot(driver, step_name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"{step_name}_{timestamp}.png"
    screenshot_path = os.path.join("screenshots", screenshot_name)

    # ایجاد پوشه screenshots در صورتی که وجود نداشته باشد
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")

    driver.save_screenshot(screenshot_path)
    with open(screenshot_path, "rb") as image_file:
        allure.attach(image_file.read(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)