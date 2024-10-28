# pages/first_page.py
from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage
from pages.select_server_page import SelectServerBottomSheet


class FirstPage(BasePage):
    def have_account(self):
        from pages.login_page import LoginPage
        have_account_button = self.find_element(AppiumBy.ID, "com.samanpr.blu.dev:id/hasAccountButton")
        have_account_button.click()

        # هدایت به صفحه لاگین
        return LoginPage(self.driver)

    def create_account(self):
        create_account_button = self.find_element(AppiumBy.ID, "com.samanpr.blu.dev:id/openAccountButton")
        create_account_button.click()

        return SelectServerBottomSheet(self.driver)
