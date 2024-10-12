# pages/box_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.dashboard.box.select_box_type_page import SelectBoxTypePage


class BoxPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.close_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/closeButton")
        self.box_page_title = (AppiumBy.ID, "com.samanpr.blu.dev:id/boxesDepositTextView")
        self.box_deposit_description = (AppiumBy.ID, "com.samanpr.blu.dev:id/boxesDepositDescriptionTextView")
        self.no_active_box_title = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        self.no_active_box_description = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        self.new_box_button = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.samanpr.blu.dev:id/fabNewSpace']")
    def close_onboarding(self):
        # صبر برای نمایش دکمه Close و کلیک روی آن
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.close_button)
        )
        self.driver.find_element(*self.close_button).click()

    def is_box_page_displayed(self):
        # بررسی نمایش صفحه باکس بعد از کلیک روی Close
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.box_page_title)
        )
        return self.driver.find_element(*self.box_page_title).is_displayed()

    def get_box_deposit_text(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.box_page_title)
        )
        return self.driver.find_element(*self.box_page_title).get_attribute("text")

    def get_box_deposit_description(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.box_deposit_description)
        )
        return self.driver.find_element(*self.box_deposit_description).get_attribute("text")

    def get_no_active_box_title(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.no_active_box_title)
        )
        return self.driver.find_element(*self.no_active_box_title).get_attribute("text")

    def get_no_active_box_description(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.no_active_box_description)
        )
        return self.driver.find_element(*self.no_active_box_description).get_attribute("text")

    def is_box_deposit_text_correct(self):
        return self.get_box_deposit_text() == "۰ ریال"

    def is_box_deposit_description_correct(self):
        return self.get_box_deposit_description() == "موجودی باکس‌ها"

    def is_no_active_box_title_correct(self):
        return self.get_no_active_box_title() == "باکس فعالی ندارید"

    def is_no_active_box_description_correct(self):
        return self.get_no_active_box_description() == "اولین باکس خود را از طریق دکمه «باکس جدید» بسازید"

    def click_new_box(self):
        # استفاده از XPath برای کلیک روی دکمه "باکس جدید"
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.new_box_button)
        ).click()
        # هدایت به صفحه انتخاب نوع باکس
        return SelectBoxTypePage(self.driver)