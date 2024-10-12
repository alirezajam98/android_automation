# pages/first_page.py
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.login_page import LoginPage


class FirstPage(BasePage):
    def have_account(self):
        have_account_button = self.find_element(AppiumBy.ID, "com.samanpr.blu.dev:id/hasAccountButton")
        have_account_button.click()

        # هدایت به صفحه لاگین
        return LoginPage(self.driver)
