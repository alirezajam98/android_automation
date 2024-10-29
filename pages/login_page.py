# pages/login_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.biometric_page import BiometricPage  # اضافه کردن BiometricPage


class LoginPage(BasePage):
    def enter_username(self, username):
        # انتظار برای نمایش عنصر
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/firstEditText"))
        )
        username_field.send_keys(username)

    def get_username_text(self):
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/firstEditText"))
        )
        return username_field.get_attribute("text")  # مستقیماً متن را برمی‌گرداند

    def enter_password(self, password):
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/secondEditText"))
        )
        password_field.send_keys(password)

    def click_login(self):

        login_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/confirm"))
        )
        login_button.click()

        # بعد از کلیک بر روی لاگین، به صفحه بیومتریک هدایت می‌شود
        return BiometricPage(self.driver)

    def click_create_account(self):
        from pages.first_page import FirstPage
        create_account_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.samanpr.blu.dev:id/openButton"))
        )
        create_account_button.click()
        return FirstPage(self.driver)