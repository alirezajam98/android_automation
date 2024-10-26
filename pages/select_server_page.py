from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.kyc.kyc_pages import CreateAccountInfoPage


class SelectServerBottomSheet(BasePage):
    def click_uat(self):
        click_uat_button = self.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className('
                                                                           '"android.view.ViewGroup").instance(3)')
        click_uat_button.click()

        return CreateAccountInfoPage(self.driver)
