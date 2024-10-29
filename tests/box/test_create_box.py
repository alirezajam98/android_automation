import json

import pytest
import allure
from utils.config import configure_logger, capture_screenshot  # ایمپورت از فایل تنظیمات
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard.box.box_profile_page import BoxProfilePage

# تنظیمات لاگ
logger = configure_logger()


# بارگذاری نسخه از فایل
with open('utils/version.json') as f:
    config = json.load(f)
    VERSION = config.get("version", "unknown_version")  # مقدار پیش‌فرض در صورت نبود نسخه



@allure.suite(f"version:{VERSION}")
@pytest.mark.order(2)
@allure.feature("Box Page")
@allure.story("Select Box Type and Create Box")
@allure.severity(allure.severity_level.BLOCKER)  # این مرحله بلاکر است
def test_select_box_type_page(login_and_dashboard):
    """تست بررسی صفحه انتخاب نوع باکس و صحت عنوان‌ها و توضیحات"""

    box_page = login_and_dashboard
    driver = box_page.driver

    # متغیر برای ذخیره نتیجه تست
    errors = []

    try:
        with allure.step("Click on box icon to open box page"):
            logger.info("کلیک روی آیکون باکس برای باز کردن صفحه باکس...")
            box_page = login_and_dashboard.click_box_icon()

        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            box_page.close_onboarding()

        # مرحله بلاکر: اگر این مرحله شکست بخورد، کل تست فیل شود
        with allure.step("Click on 'New Box' button (BLOCKER)"):
            logger.info("کلیک روی دکمه 'باکس جدید'...")
            select_box_type_page = box_page.click_new_box()
            assert select_box_type_page.is_page_displayed(), "صفحه انتخاب نوع باکس نمایش داده نشده است."
            logger.info("وارد صفحه انتخاب نوع باکس شدید.")
    except Exception as e:
        logger.error(f"خطای بلاکر: {e}")
        capture_screenshot(driver, "select_box_type_page_blocker_error")
        raise AssertionError(f"Blocker error: {e}")

    # سایر مراحل: در صورت خطا، اسکرین‌شات بگیرید اما تست ادامه پیدا کند
    try:
        with allure.step("Check normal box title and description"):
            assert select_box_type_page.is_normal_box_title_correct(), "عنوان 'بلوباکس' نادرست است."
            assert select_box_type_page.is_normal_box_description_correct(), "توضیح 'بلوباکس' نادرست است."
            logger.info("بررسی عنوان و توضیحات باکس عادی...")
    except AssertionError as e:
        errors.append(f"خطا در بررسی عنوان/توضیحات باکس عادی: {e}")
        logger.error(f"Error in normal box title/description: {e}")
        capture_screenshot(driver, "normal_box_title_description_error")

    try:
        with allure.step("Check long term box title and description"):
            assert select_box_type_page.is_long_term_box_title_correct(), "عنوان 'بیگ‌باکس' نادرست است."
            assert select_box_type_page.is_long_term_box_description_correct(), "توضیح 'بیگ‌باکس' نادرست است."
            logger.info("بررسی عنوان و توضیحات باکس بلند مدت...")
    except AssertionError as e:
        errors.append(f"خطا در بررسی عنوان/توضیحات باکس بلند مدت: {e}")
        logger.error(f"Error in long term box title/description: {e}")
        capture_screenshot(driver, "long_term_box_title_description_error")

    try:
        with allure.step("Select normal box"):
            logger.info("انتخاب باکس عادی (بلوباکس)...")
            create_box_page = select_box_type_page.select_normal_box()
    except Exception as e:
        errors.append(f"خطا در انتخاب باکس عادی: {e}")
        logger.error(f"Error in selecting normal box: {e}")
        capture_screenshot(driver, "select_normal_box_error")

    try:
        with allure.step("Enter box name and save"):
            logger.info("ورود نام باکس و ذخیره...")
            create_box_page.enter_box_name("My Test Box1")
            create_box_page.save_new_box()
    except Exception as e:
        errors.append(f"خطا در ورود نام باکس: {e}")
        logger.error(f"Error in entering box name: {e}")
        capture_screenshot(driver, "enter_box_name_error")

    try:
        with allure.step("Check if the box profile page is displayed"):
            box_profile_page = BoxProfilePage(create_box_page.driver)
            WebDriverWait(create_box_page.driver, 20).until(
                EC.visibility_of_element_located(box_profile_page.deposit_button)
            )
            assert box_profile_page.get_deposit_btn_text(), "باکس ایجاد نشد یا به صفحه پروفایل باکس هدایت نشدید."
            logger.info("باکس با موفقیت ایجاد شد.")
    except Exception as e:
        errors.append(f"خطا در ایجاد باکس: {e}")
        logger.error(f"Error in box creation: {e}")
        capture_screenshot(driver, "box_creation_error")

    # در صورت وجود هرگونه خطا، گزارش خطاها
    if errors:
        raise AssertionError("Errors encountered during test:\n" + "\n".join(errors))
