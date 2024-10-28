from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.dashboard.box.box_page import BoxPage  # وارد کردن کلاس صفحه اصلی باکس
from pages.dashboard.box.box_profile_page import BoxProfilePage  # وارد کردن کلاس صفحه پروفایل باکس


class BoxConfirmModal(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.title = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        self.subtitle = (AppiumBy.ID, "com.samanpr.blu.dev:id/subtitleTextView")
        self.description = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        self.delete_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/deleteButton")
        self.cancel_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/cancelButton")

    def is_modal_displayed(self):
        """بررسی نمایش مودال تأیید حذف"""
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.title)
        )
        return self.driver.find_element(*self.title).is_displayed()

    def get_title_text(self):
        """دریافت عنوان مودال"""
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.title)
        )
        return self.driver.find_element(*self.title).get_attribute("text")

    def get_subtitle_text(self):
        """دریافت زیرعنوان مودال"""
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.subtitle)
        )
        return self.driver.find_element(*self.subtitle).get_attribute("text")

    def get_description_text(self):
        """دریافت توضیحات مودال"""
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.description)
        )
        return self.driver.find_element(*self.description).get_attribute("text")

    def cancel_delete(self):
        """کلیک روی دکمه کنسل و بازگشت به صفحه پروفایل باکس"""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.cancel_button)
        ).click()
        return BoxProfilePage(self.driver)  # بازگشت به صفحه پروفایل باکس

    def confirm_delete(self):
        """کلیک روی دکمه تأیید حذف و هدایت به صفحه اصلی باکس"""
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()
        return BoxPage(self.driver)  # بازگشت به صفحه اصلی باکس
