# pages/create_box_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.dashboard.box.box_profile_page import BoxProfilePage
from tests.box.test_box import logger


class CreateBoxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.box_name_field = (AppiumBy.XPATH, "//android.widget.EditText["
                                               "@resource-id='com.samanpr.blu.dev:id/spaceNameEditText']")
        self.save_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/confirmButton")

    def enter_box_name(self, box_name):
        # وارد کردن نام باکس
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.box_name_field)
        ).send_keys(box_name)


    def save_new_box(self):
        # کلیک روی دکمه ذخیره باکس
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
        return BoxProfilePage(self.driver)

    def is_page_displayed(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.box_name_field)
        )
        return self.driver.find_element(*self.box_name_field).is_displayed()

    def close_keyboard(self):
        # بررسی می‌کند که آیا کیبورد باز است، سپس آن را می‌بندد
        try:
            self.driver.hide_keyboard()
            logger.info("کیبورد بسته شد.")
        except Exception as e:
            logger.warning(f"کیبورد بسته نشد یا باز نبود: {str(e)}")