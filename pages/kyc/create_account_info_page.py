from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class CreateAccountInfoPage(BasePage):
    def click_start(self):
        start_button = self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "com.samanpr.blu.dev:id/confirm")
        start_button.click()

        # هدایت به صفحه لاگین
