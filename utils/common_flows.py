import logging
import allure
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.kyc.kyc_pages import NotificationPermissionPage, OpenAccountPage, SelectServerPage, \
    CreateAccountInfoPage, AcceptRulesAndRegulations, EnterPhoneNumberPage, ReferralPage, NationalCodePage, \
    BirthDatePage, UserNamePage, PasswordPage, CreateAccountInBluStatePage
from utils.config import capture_screenshot  # تنظیمات لاگ و تابع اسکرین‌شات

# تنظیمات لاگ
logger = logging.getLogger(__name__)


# تابعی برای بارگذاری فایل JSON


def setup_user_account_creation_steps(driver, phone_number, national_code, username, text_reference):
    accept_page = AcceptRulesAndRegulations(driver)

    # افزودن اطلاعات کاربر به عنوان پارامترهای اولیه در گزارش Allure
    with allure.step("User Information Setup") as step:
        allure.dynamic.parameter("Phone Number", phone_number)
        allure.dynamic.parameter("National Code", national_code)
        allure.dynamic.parameter("Username", username)
        logger.info(
            f"Generated user info - Phone Number: {phone_number}, National Code: {national_code}, Username: {username}")

    try:
        # مرحله 1: بررسی دسترسی نوتیفیکیشن
        notification_permission_page = NotificationPermissionPage(driver)
        notification_permission_page.allow_notification_permission()
        logger.info("Clicked on 'Allow' button for notification permission.")

        # مرحله 2: کلیک روی دکمه 'ایجاد حساب کاربری'
        with allure.step("Click on 'Create Account' button"):
            try:
                logger.info("کلیک روی دکمه 'ایجاد حساب کاربری'...")
                create_account_button = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
                )
                create_account_button.click()
                logger.info("دکمه 'ایجاد حساب کاربری' کلیک شد.")
            except TimeoutException:
                logger.info("No nCreate Account button displayed, continuing.")

        # مرحله 3: بررسی دوباره نوتیفیکیشن (در صورت لزوم)
        try:
            notification_permission_page = NotificationPermissionPage(driver)
            notification_permission_page.allow_notification_permission()
            logger.info("Clicked on 'Allow' button for notification permission.")
        except TimeoutException:
            logger.info("No notification permission modal displayed, continuing.")

        # مرحله 4: کلیک روی دکمه 'باز کردن حساب'
        with allure.step("Click on 'Open Account' button"):
            logger.info("کلیک روی دکمه 'باز کردن حساب'...")
            open_account_page = OpenAccountPage(driver)
            open_account_page.click_open_account()
            logger.info("دکمه 'باز کردن حساب' کلیک شد.")

        # مرحله 5: انتخاب سرور 'UAT'
        with allure.step("Select 'UAT' from server selection"):
            logger.info("انتخاب سرور 'UAT'...")
            select_server_page = SelectServerPage(driver)
            select_server_page.select_uat_server()
            logger.info("سرور 'UAT' انتخاب شد.")
            # بررسی متن "create_account_info_page" اما اگر اشتباه بود، ادامه پیدا کند

        with allure.step("Check 'create_account_info_page' text"):
            try:
                expected_text = text_reference["kyc_pages"]["create_account_info_page_title"]
                create_account_info_page = CreateAccountInfoPage(driver)
                actual_text = create_account_info_page.get_account_info_page_title()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن تایتل برای صفحه توضیحات صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن تایتل صفحه توضیحات: {e}")

                # گرفتن اسکرین‌شات و افزودن به گزارش
                screenshot_path = capture_screenshot(driver, "account_info_title_mismatch")
                allure.attach.file(screenshot_path, name="Mismatch Screenshot",
                                   attachment_type=allure.attachment_type.PNG)

                # اضافه کردن متن خطا به گزارش
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)

                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم

            # بررسی متن "clock_title_info_page" اما اگر اشتباه بود، ادامه پیدا کند
        with allure.step("Check 'clock_title_info_page' text"):
            try:
                expected_text = text_reference["kyc_pages"]["clock_title_info_page"]
                create_account_info_page = CreateAccountInfoPage(driver)
                actual_text = create_account_info_page.get_clock_text_title()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن صفحه توضیحات صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن ساعت صفحه توضیحات: {e}")
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)
                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم

        with allure.step("Check 'clock_subtitle_info_page' text"):
            try:
                expected_text = text_reference["kyc_pages"]["clock_subtitle_info_page"]
                create_account_info_page = CreateAccountInfoPage(driver)
                actual_text = create_account_info_page.get_clock_text_subtitle()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن صفحه توضیحات صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن ساعت صفحه توضیحات: {e}")
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)
                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم

        with allure.step("Check 'sim_title_info_page' text"):
            try:
                expected_text = text_reference["kyc_pages"]["sim_title_info_page"]
                create_account_info_page = CreateAccountInfoPage(driver)
                actual_text = create_account_info_page.get_sim_text_title()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن صفحه توضیحات صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن سیم کارت صفحه توضیحات: {e}")
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)
                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم

        with allure.step("Check 'sim_subtitle_info_page' text"):
            try:
                expected_text = text_reference["kyc_pages"]["sim_subtitle_info_page"]
                create_account_info_page = CreateAccountInfoPage(driver)
                actual_text = create_account_info_page.get_sim_text_subtitle()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن صفحه توضیحات صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن سیم کارت صفحه توضیحات: {e}")
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)
                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم

        with allure.step("Check 'identification_documents_title_info_page' text"):
            try:
                expected_text = text_reference["kyc_pages"]["identification_documents_title_info_page"]
                create_account_info_page = CreateAccountInfoPage(driver)
                actual_text = create_account_info_page.get_identification_documents_text_title()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن صفحه توضیحات صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن مدارک لازم صفحه توضیحات: {e}")
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)
                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم

        with allure.step("Check 'identification_documents_subtitle_info_page' text"):
            try:
                expected_text = text_reference["kyc_pages"]["identification_documents_subtitle_info_page"]
                create_account_info_page = CreateAccountInfoPage(driver)
                actual_text = create_account_info_page.get_identification_documents_text_subtitle()
                assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
                logger.info(f"متن صفحه توضیحات صحیح است: {actual_text}")
            except AssertionError as e:
                logger.error(f"خطا در بررسی متن مدارک لازم صفحه توضیحات: {e}")
                allure.attach(f"Expected: {expected_text}\nActual: {actual_text}", "Mismatch in text",
                              allure.attachment_type.TEXT)
                # خطا را لاگ می‌کنیم اما ادامه می‌دهیم
        # مرحله 6: کلیک روی دکمه 'شروع'
        with allure.step("Click on 'Start' button"):
            logger.info("کلیک روی دکمه 'شروع'...")
            create_account_info_page = CreateAccountInfoPage(driver)
            create_account_info_page.click_start()
            logger.info("دکمه 'شروع' کلیک شد.")

        # مرحله 7: بررسی و تغییر وضعیت سوییچ
        with allure.step("Check and toggle the agreement switch"):
            initial_status = accept_page.is_switch_on()
            logger.info(f"Initial switch status: {'ON' if initial_status else 'OFF'}")
            accept_page.toggle_switch()
            new_status = accept_page.is_switch_on()
            logger.info(f"Switch status after toggle: {'ON' if new_status else 'OFF'}")

        # مرحله 8: کلیک روی دکمه 'تایید' و رفتن به مرحله وارد کردن شماره تلفن
        with allure.step("Click confirm button after toggle"):
            logger.info("کلیک روی دکمه 'تایید'...")
            accept_page.click_confirm_button()
            logger.info("دکمه 'تایید' کلیک شد و به صفحه وارد کردن شماره تلفن هدایت شد.")

        # مرحله 9: وارد کردن شماره تلفن
        with allure.step("Enter phone number"):
            phone_page = EnterPhoneNumberPage(driver)
            phone_page.enter_phone_number(phone_number)
            logger.info(f"شماره تلفن وارد شد: {phone_number}")

        # مرحله 10: کلیک روی دکمه 'بعدی'
        with allure.step("Click next button"):
            phone_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        # مرحله 11: بررسی متن ریفرال
        with allure.step("Check 'مانند:‌ MDMGKP' text"):
            expected_text = text_reference["kyc_pages"]["referralInputEditText"]
            referral_page = ReferralPage(driver)
            actual_text = referral_page.get_referral_field_text()
            assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
            logger.info(f"متن ریفرال صحیح است: {actual_text}")

        with allure.step("Click next button"):
            referral_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        # مرحله 12: بررسی و وارد کردن کد ملی
        with allure.step("Check 'کد ملی ۱۰ رقمی' text"):
            expected_text = text_reference["kyc_pages"]["national_code"]
            national_page = NationalCodePage(driver)
            actual_text = national_page.get_national_code_text()
            assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"
            logger.info(f"متن کد ملی صحیح است: {actual_text}")

        with allure.step("Enter national code"):
            national_page.enter_national_code(national_code)
            logger.info(f"کدملی وارد شد: {national_code}")

        with allure.step("Click next button"):
            national_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        # مرحله 13: اسکرول کردن سال
        with allure.step("Scroll year field"):
            birth_date_page = BirthDatePage(driver)
            birth_date_page.scroll_year()  # اسکرول کردن سال
            logger.info("سال با موفقیت اسکرول شد.")

        with allure.step("Click next button"):
            birth_date_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        # مرحله 14: وارد کردن نام کاربری
        with allure.step("Enter new username"):
            username_page = UserNamePage(driver)
            username_page.enter_username(username)
            logger.info(f"نام کاربری وارد شد: {username}")

        with allure.step("Click next button"):
            username_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        # مرحله 15: وارد کردن رمز عبور
        with allure.step("Enter password"):
            password_page = PasswordPage(driver)
            password_page.enter_password("Aa123456")
            logger.info("رمز عبور وارد شد.")

        with allure.step("Click next button"):
            password_page.click_next_button()
            logger.info("دکمه 'بعدی' کلیک شد.")

        # مرحله 16: تایید وضعیت حساب کاربری در Blu
        with allure.step("Click next button"):
            create_account_in_blu_state_page = CreateAccountInBluStatePage(driver)
            create_account_in_blu_state_page.click_confirm_button()
            logger.info("دکمه 'ادامه' کلیک شد.")
    except Exception as e:

        logger.error(f"خطا رخ داد: {e}")
        # اسکرین‌شات در صورت بروز هرگونه خطا
        screenshot_path = capture_screenshot(driver, "account_creation_error")
        allure.attach.file(screenshot_path, name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
        raise e
