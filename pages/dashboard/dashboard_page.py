# pages/dashboard_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.dashboard.box.box_page import BoxPage
from pages.setting.settings_page import SettingsPage


class DashboardPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.title_dashboard = (AppiumBy.CLASS_NAME, "com.samanpr.blu.dev:id/toolbarTitleTextView")
        self.title_dashboard_by_id = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        self.search_btn = (AppiumBy.ID, "com.samanpr.blu.dev:id/searchButton")
        self.top_up_btn = (AppiumBy.ID, "com.samanpr.blu.dev:id/chargeButton")
        self.top_up_txt = (AppiumBy.XPATH,
                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                           ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat"
                           ".widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout"
                           "/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout"
                           "/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.TextView")
        self.box_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/boxButton")
        self.box_btn_txt = (AppiumBy.XPATH,
                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                            ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                            ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat"
                            ".widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout"
                            "/android.widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout"
                            "/android.view.ViewGroup/android.view.ViewGroup[3]/android.widget.TextView")
        self.settings_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/nav_settings")  # ID دکمه تنظیمات

    def get_title(self):
        get_title_dashboard = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.title_dashboard)
        )
        return get_title_dashboard.get_attribute("text")

    def is_charge_button_displayed(self):
        try:
            return self.driver.find_element(*self.box_button).is_displayed()
        except:
            return False

    def click_box_icon(self):
        self.click(self.box_button)
        return BoxPage(self.driver)  # هدایت به صفحه باکس

    def click_settings_button(self):
        # انتظار برای نمایش دکمه تنظیمات و کلیک روی آن
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.settings_button)
        ).click()
        return SettingsPage(self.driver)  # هدایت به صفحه پروفایل (تنظیمات)
