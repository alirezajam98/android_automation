# pages/biometric_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.dashboard.dashboard_page import DashboardPage

class BiometricPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.btn_not_now = (AppiumBy.ID, "com.samanpr.blu.dev:id/btnNotNow")

    def check_not_now(self):
        # افزایش زمان انتظار و استفاده از visibility_of_element_located
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(self.btn_not_now)  # منتظر می‌ماند تا عنصر قابل مشاهده و قابل تعامل شود
            )
            return self.driver.find_element(*self.btn_not_now).is_displayed()
        except:
            return False

    def click_not_now(self):
        self.click(self.btn_not_now)
        return DashboardPage(self.driver)
