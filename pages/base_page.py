# pages/base_page.py
from appium.webdriver.common.appiumby import AppiumBy

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by: AppiumBy, value: str):
        return self.driver.find_element(by, value)

    def click(self, locator):
        # پیدا کردن عنصر و کلیک بر روی آن
        element = self.driver.find_element(*locator)
        element.click()
