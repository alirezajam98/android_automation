import json
import allure
import pytest
from logging_config import logger


# تابعی برای بارگذاری فایل JSON
def load_text_reference():
    with open('text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@pytest.mark.order(1)
@allure.feature("Settings Page")
@allure.story("Verify settings page texts")
def test_check_settings_texts(login_and_dashboard):
    """تست لاگین و بررسی صحت متون صفحه تنظیمات"""

    dashboard_page = login_and_dashboard

    # رفتن به صفحه تنظیمات
    settings_page = dashboard_page.click_settings_button()

    # بررسی اینکه صفحه تنظیمات نمایش داده شده است
    assert settings_page.is_page_displayed(), "صفحه تنظیمات نمایش داده نشد."

    # خواندن متون مرجع از فایل JSON
    text_reference = load_text_reference()

    # بررسی نام کاربر و شماره تلفن
    user_name = settings_page.get_user_name()
    phone_number = settings_page.get_phone_number()

    # افزودن لاگ‌ها و مقایسه مقادیر
    logger.info(f"نام کاربر: {user_name}")
    logger.info(f"شماره تلفن: {phone_number}")

    # متغیر برای ذخیره نتیجه تست
    errors = []

    # بررسی مقادیر با مرجع و ثبت خطاها به جای متوقف کردن تست
    try:
        assert user_name == text_reference["settings_page"]["username_label"], \
            f"User name mismatch: expected '{text_reference['settings_page']['username_label']}', got '{user_name}'"
    except AssertionError as e:
        logger.error(str(e))
        errors.append(str(e))

    try:
        assert phone_number == text_reference["settings_page"]["phone_number_label"], \
            f"Phone number mismatch: expected '{text_reference['settings_page']['phone_number_label']}', got '{phone_number}'"
    except AssertionError as e:
        logger.error(str(e))
        errors.append(str(e))

    # اگر خطاهایی ثبت شده‌اند، در انتهای تست آن‌ها را گزارش کنید
    if errors:
        raise AssertionError("Errors encountered during test:\n" + "\n".join(errors))

    logger.info("All texts in settings page are correct.")
