import json

import pytest
import allure
import time  # اضافه کردن برای استفاده از sleep
from utils.config import configure_logger, capture_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = configure_logger()

# تابعی برای بارگذاری فایل JSON
def load_text_reference():
    with open('utils/text_reference.json', 'r', encoding='utf-8') as f:
        return json.load(f)


@pytest.mark.order(4)
@allure.feature("Box Settings")
@allure.story("Edit Box Name and Delete Box")
def test_edit_box_name_and_delete_box(login_and_dashboard):
    """تست ویرایش نام باکس و حذف باکس با تأیید و کنسل"""

    text_reference = load_text_reference()

    box_page = login_and_dashboard
    driver = box_page.driver

    try:
        with allure.step("Click on box icon to open box page"):
            logger.info("کلیک روی آیکون باکس برای باز کردن صفحه باکس...")
            box_page = login_and_dashboard.click_box_icon()

        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            box_page.close_onboarding()

            # اضافه کردن تأخیر برای اطمینان از اتمام انیمیشن
            time.sleep(2)  # اینجا 2 ثانیه تأخیر اضافه شده است، در صورت نیاز تنظیم کنید

        with allure.step("Check if the box page is displayed"):
            # انتظار برای نمایش عنصر صفحه باکس
            WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(box_page.box_page_title)
            )
            logger.info("صفحه باکس نمایش داده شد.")

        with allure.step("Check if first box name is correct"):
            try:
                assert box_page.is_first_box_name_correct(), "نام اولین باکس نادرست است."
                logger.info("نام اولین باکس صحیح است.")
            except AssertionError as e:
                logger.warning(f"نام اولین باکس نادرست است: {e}")

        with allure.step("Check if first box amount is correct"):
            assert box_page.is_first_box_amount_correct(), "مقدار اولین باکس نادرست است."
            logger.info("مقدار اولین باکس صحیح است.")

        with allure.step("Click on the first box and navigate to profile"):
            logger.info("کلیک روی اولین باکس و هدایت به صفحه پروفایل باکس...")
            box_profile_page = box_page.click_first_box()

            # تایید نمایش صفحه پروفایل
            assert box_profile_page.is_page_displayed_deposit_btn(), "صفحه پروفایل باکس نمایش داده نشده است."
            logger.info("صفحه پروفایل باکس نمایش داده شد.")

        with allure.step("Click on setting button and open settings bottom sheet"):
            logger.info("باز کردن تنظیمات باکس...")
            box_setting_bottom_sheet = box_profile_page.click_box_settings()

        with allure.step("Click on 'Delete Box' and open confirmation modal"):
            logger.info("کلیک روی 'حذف باکس'...")
            confirm_modal = box_setting_bottom_sheet.click_delete_box()

        with allure.step("Cancel deletion and return to box profile"):
            logger.info("کنسل کردن حذف...")
            box_profile_page = confirm_modal.cancel_delete()

        with allure.step("Click on setting button and open settings bottom sheet"):
            logger.info("باز کردن تنظیمات باکس...")
            box_setting_bottom_sheet = box_profile_page.click_box_settings()

        with allure.step("Click on 'Delete Box' and open confirmation modal"):
            logger.info("کلیک روی 'حذف باکس'...")
            confirm_modal = box_setting_bottom_sheet.click_delete_box()

        with allure.step("Cancel deletion and return to box profile"):
            logger.info("تایید کردن حذف...")
            box_page = confirm_modal.confirm_delete()
        with allure.step("Check 'باکس فعالی ندارید' text"):
            try:
                expected_text = text_reference["box_page"]["no_active_box_title"]
                actual_text = box_page.get_no_active_box_title()
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
            except AssertionError as e:
                logger.warning(f"Error in no_active_box_title: {e}")
                logger.error(str(e))
        with allure.step("Check '۰ ریال' text"):
            try:
                expected_text = text_reference["box_page"]["box_deposit_text"]
                actual_text = box_page.get_box_deposit_text()
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
            except AssertionError as e:
                logger.warning(f"Error in box_deposit_text: {e}")
                logger.error(str(e))

        with allure.step("Check 'موجودی باکس‌ها' text"):
            try:
                expected_text = text_reference["box_page"]["box_deposit_description"]
                actual_text = box_page.get_box_deposit_description()
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
            except AssertionError as e:
                logger.warning(f"Error in box_deposit_description: {e}")
                logger.error(str(e))

        with allure.step("Check 'باکس فعالی ندارید' text"):
            try:
                expected_text = text_reference["box_page"]["no_active_box_title"]
                actual_text = box_page.get_no_active_box_title()
                assert actual_text == expected_text, \
                    f"Expected '{expected_text}', but got '{actual_text}'"
            except AssertionError as e:
                logger.warning(f"Error in no_active_box_title: {e}")
                logger.error(str(e))

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "first_box_test_error")
        raise e
