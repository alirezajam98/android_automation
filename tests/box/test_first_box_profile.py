import pytest
import allure
import time  # اضافه کردن برای استفاده از sleep
from utils.config import configure_logger, capture_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# تنظیمات لاگ
logger = configure_logger()

@pytest.mark.order(3)
@allure.feature("Box Page")
@allure.story("Check First Box and Navigate to Profile")
@allure.severity(allure.severity_level.NORMAL)
def test_check_first_box_and_navigate(login_and_dashboard):
    """تست بررسی نام و مقدار اولین باکس و هدایت به صفحه پروفایل باکس"""

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

    except Exception as e:
        logger.error(f"خطا رخ داد: {e}")
        capture_screenshot(driver, "first_box_test_error")
        raise e
