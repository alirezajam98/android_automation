from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.dashboard.box.box_setting_bottom_sheet import BoxSettingBottomSheet


class BoxProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.toolbar = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                        "/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                        ".FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.view.ViewGroup[1]/android.widget.TextView")
        self.back_to_box_page = (AppiumBy.ACCESSIBILITY_ID, "رفتن به بالا")
        self.box_profile_name = (AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                                 ".ViewGroup/android.widget.TextView")
        self.avatar_image = (AppiumBy.ID, "com.samanpr.blu.dev:id/avatarImageView")
        self.save_amount = (AppiumBy.ID, "com.samanpr.blu.dev:id/priceTextView")
        self.desc_amount = (AppiumBy.XPATH,
                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                            ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                            ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                            ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                            ".LinearLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.TextView[2]")
        self.deposit_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/depositButton")
        self.withdraw_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/withdrawButton")
        self.setting_button = (AppiumBy.ID, "com.samanpr.blu.dev:id/settingsButton")
        self.image_goal = (AppiumBy.XPATH,
                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                           ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                           ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.View[1]")
        self.title_goal = (AppiumBy.XPATH,
                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                           ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                           ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                           ".LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup["
                           "1]/android.widget.TextView[1]")
        self.status_goal_active = (AppiumBy.XPATH,
                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                                   ".widget.ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup["
                                   "1]/android.view.View[2]")
        self.status_goal = (AppiumBy.XPATH,
                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                            ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                            ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                            ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                            ".LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.view.View[4]")
        self.activation_goal_desc = (AppiumBy.XPATH,
                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                     ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                     "/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                     ".FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android"
                                     ".widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup["
                                     "2]/android.view.ViewGroup[1]/android.widget.TextView[2]")
        self.add_goal_button = (AppiumBy.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup["
                                "1]/android.widget.ImageView[2]")
        self.image_round_up = (AppiumBy.XPATH,
                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                               ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                               ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                               ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                               ".LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.View[1]")
        self.title_round_up = (AppiumBy.XPATH,
                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                               ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                               ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                               ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                               ".LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup["
                               "2]/android.widget.TextView[1]")
        self.status_round_up = (AppiumBy.XPATH,
                                "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                ".ScrollView/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                ".LinearLayout/android.view.ViewGroup[2]/android.view.ViewGroup[2]/android.view.View["
                                "4]")
        self.activation_round_up_desc = (AppiumBy.XPATH,
                                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                         ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                         "/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                         ".FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android"
                                         ".widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup["
                                         "2]/android.view.ViewGroup[2]/android.widget.TextView[2]")
        self.transaction_title = (AppiumBy.ID, "com.samanpr.blu.dev:id/transactionTitleTextView")
        self.empty_state_image = (AppiumBy.ID, "com.samanpr.blu.dev:id/illustrationView")
        self.empty_state_desc = (AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".ScrollView/android.widget.ScrollView/android.widget.FrameLayout/androidx.appcompat"
                                 ".widget.LinearLayoutCompat/android.widget.TextView[1]")
        self.empty_state_desc_1 = (AppiumBy.XPATH,
                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                   ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android"
                                   ".widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android"
                                   ".widget.ScrollView/android.widget.ScrollView/android.widget.FrameLayout/androidx"
                                   ".appcompat.widget.LinearLayoutCompat/android.widget.TextView[2]")

    def get_active_goal_status(self):
        return self.driver.find_element(*self.status_goal_active).get_attribute("text")

    def click_box_settings(self):
        self.driver.find_element(*self.setting_button).click()
        return BoxSettingBottomSheet(self.driver)

    def click_back_to_box_page(self):
        self.driver.find_element(*self.back_to_box_page).click()

    def get_box_profile_title(self):
        return self.driver.find_element(*self.box_profile_name).get_attribute("text")

    def check_image_box_profile(self):
        return self.driver.find_element(*self.avatar_image).is_displayed()

    def get_save_amount(self):
        return self.driver.find_element(*self.save_amount).get_attribute("text")

    def check_save_amount(self):
        return self.driver.find_element(*self.save_amount).is_displayed()

    def get_desc_amount(self):
        return self.driver.find_element(*self.desc_amount).get_attribute("text")

    # def get_deposit_btn_text(self):
    #     return self.driver.find_element(*self.deposit_button).get_attribute("text")
    def get_deposit_btn_text(self):
        # بررسی عنوان "بلوباکس"
        return self.driver.find_element(*self.deposit_button).text == "واریز"

    def is_page_displayed_deposit_btn(self):
        return self.driver.find_element(*self.deposit_button).is_displayed()

    def click_deposit_btn(self):
        self.driver.find_element(*self.deposit_button).click()

    def get_withdraw_btn_text(self):
        return self.driver.find_element(*self.withdraw_button).get_attribute("text")

    def click_withdraw_btn(self):
        self.driver.find_element(*self.withdraw_button).click()

    def check_setting_button(self):
        return self.driver.find_element(*self.setting_button).is_displayed()

    def check_image_goal(self):
        return self.driver.find_element(*self.image_goal).is_displayed()

    def get_goal_title(self):
        return self.driver.find_element(*self.title_goal).get_attribute("text")

    def get_activation_goal_desc(self):
        return self.driver.find_element(*self.activation_goal_desc).get_attribute("text")

    def get_status_goal(self):
        return self.driver.find_element(*self.status_goal).get_attribute("text")

    def check_add_goal_button(self):
        return self.driver.find_element(*self.add_goal_button).is_displayed()

    def check_image_round_up(self):
        return self.driver.find_element(*self.image_round_up).is_displayed()

    def get_round_up_title(self):
        return self.driver.find_element(*self.title_round_up).get_attribute("text")

    def get_activation_round_up_desc(self):
        return self.driver.find_element(*self.activation_round_up_desc).get_attribute("text")

    def get_status_round_up(self):
        return self.driver.find_element(*self.status_round_up).get_attribute("text")

    def get_title_transaction_box_profile(self):
        return self.driver.find_element(*self.transaction_title).get_attribute("text")

    def check_empty_state_image(self):
        return self.driver.find_element(*self.empty_state_image).is_displayed()

    def get_empty_state_desc(self):
        return self.driver.find_element(*self.empty_state_desc).get_attribute("text")

    def get_empty_state_desc_1(self):
        return self.driver.find_element(*self.empty_state_desc_1).get_attribute("text")

    # More methods can be added following the same pattern.

