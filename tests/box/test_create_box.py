import pytest
import allure
from utils.config import configure_logger, capture_screenshot  # ایمپورت از فایل تنظیمات
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard.box.box_profile_page import BoxProfilePage

# تنظیمات لاگ
logger = configure_logger()


@pytest.mark.order(2)
@allure.feature("Box Page")
@allure.story("Select Box Type and Create Box")
@allure.severity(allure.severity_level.BLOCKER)
def test_select_box_type_page(login_and_dashboard):
    """تست بررسی صفحه انتخاب نوع باکس و صحت عنوان‌ها و توضیحات"""

    box_page = login_and_dashboard
    driver = box_page.driver

    try:
        with allure.step("Click on box icon to open box page"):
            logger.info("کلیک روی آیکون باکس برای باز کردن صفحه باکس...")
            box_page = login_and_dashboard.click_box_icon()

        with allure.step("Close the onboarding page"):
            logger.info("بستن صفحه انبوردینگ...")
            box_page.close_onboarding()

        with allure.step("Click on 'New Box' button"):
            logger.info("کلیک روی دکمه 'باکس جدید'...")
            select_box_type_page = box_page.click_new_box()

        with allure.step("Check if 'Select Box Type' page is displayed"):
            assert select_box_type_page.is_page_displayed(), "صفحه انتخاب نوع باکس نمایش داده نشده است."
            logger.info("وارد صفحه انتخاب نوع باکس شدید.")

        with allure.step("Check normal box title and description"):
            assert select_box_type_page.is_normal_box_title_correct(), "عنوان 'بلوباکس' نادرست است."
            assert select_box_type_page.is_normal_box_description_correct(), "توضیح 'بلوباکس' نادرست است."
            logger.info("بررسی عنوان و توضیحات باکس عادی...")

        with allure.step("Check long term box title and description"):
            assert select_box_type_page.is_long_term_box_title_correct(), "عنوان 'بیگ‌باکس' نادرست است."
            assert select_box_type_page.is_long_term_box_description_correct(), "توضیح 'بیگ‌باکس' نادرست است."
            logger.info("بررسی عنوان و توضیحات باکس بلند مدت...")

        with allure.step("Select normal box"):
            logger.info("انتخاب باکس عادی (بلوباکس)...")
            create_box_page = select_box_type_page.select_normal_box()

        with allure.step("Enter box name and save"):
            logger.info("ورود نام باکس و ذخیره...")
            create_box_page.enter_box_name("My Test Box1")
            create_box_page.save_new_box()

        with allure.step("Check if the box profile page is displayed"):
            box_profile_page = BoxProfilePage(create_box_page.driver)
            WebDriverWait(create_box_page.driver, 20).until(
                EC.visibility_of_element_located(box_profile_page.deposit_button)
            )
            assert box_profile_page.get_deposit_btn_text(), "باکس ایجاد نشد یا به صفحه پروفایل باکس هدایت نشدید."
            logger.info("باکس با موفقیت ایجاد شد.")

    except AssertionError as e:
        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "select_box_type_page_error")
        raise e
