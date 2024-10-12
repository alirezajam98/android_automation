from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SettingsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.Layout = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                       ".FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget"
                                       ".FrameLayout[1]")
        self.QRscan = (AppiumBy.ACCESSIBILITY_ID, "رفتن به بالا")
        self.SettingTitle = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                             "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                             ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout"
                                             "/android.widget.FrameLayout/androidx.appcompat.widget"
                                             ".LinearLayoutCompat/android.widget.FrameLayout["
                                             "1]/android.widget.FrameLayout/android.widget.ScrollView/android.widget"
                                             ".LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android"
                                             ".view.ViewGroup[1]/android.widget.TextView")
        self.ShareButton = (AppiumBy.ID, "com.samanpr.blu.dev:id/actionShare")
        self.ImageView = (AppiumBy.ID, "com.samanpr.blu.dev:id/avatarImageView")
        self.UserName = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        self.PhoneNumber = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")
        self.SettingSegmentTitle = (AppiumBy.ID, "com.samanpr.blu.dev:id/headerTitleTextView")
        self.SettingAccountTitle = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".FrameLayout/android.widget.FrameLayout/android.widget"
                                                    ".FrameLayout/androidx.appcompat.widget.LinearLayoutCompat"
                                                    "/android.widget.FrameLayout["
                                                    "1]/android.widget.FrameLayout/android.widget.ScrollView/androidx"
                                                    ".appcompat.widget.LinearLayoutCompat/android.widget.ScrollView"
                                                    "/androidx.appcompat.widget.LinearLayoutCompat/androidx"
                                                    ".recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                                    "1]/android.widget.TextView[1]")
        self.SettingAccountDesc = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                   ".widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                                   ".FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget"
                                                   ".LinearLayoutCompat/android.widget.FrameLayout["
                                                   "1]/android.widget.FrameLayout/android.widget.ScrollView/androidx"
                                                   ".appcompat.widget.LinearLayoutCompat/android.widget.ScrollView"
                                                   "/androidx.appcompat.widget.LinearLayoutCompat/androidx"
                                                   ".recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                                   "1]/android.widget.TextView[2]")
        self.SettingPrivacyTitle = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".FrameLayout/android.widget.FrameLayout/android.widget"
                                                    ".FrameLayout/androidx.appcompat.widget.LinearLayoutCompat"
                                                    "/android.widget.FrameLayout["
                                                    "1]/android.widget.FrameLayout/android.widget.ScrollView/androidx"
                                                    ".appcompat.widget.LinearLayoutCompat/android.widget.ScrollView"
                                                    "/androidx.appcompat.widget.LinearLayoutCompat/androidx"
                                                    ".recyclerview.widget.RecyclerView/android.view.ViewGroup["
                                                    "2]/android.widget.TextView[1]")
        self.SettingPrivacyDesc = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                   ".widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                                   ".FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget"
                                                   ".LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget"
                                                   ".FrameLayout/android.widget.ScrollView/androidx.appcompat.widget"
                                                   ".LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat"
                                                   ".widget.LinearLayoutCompat/androidx.recyclerview.widget"
                                                   ".RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[2]")
        self.SettingNotifyTitle = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                   ".widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                                   ".FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget"
                                                   ".LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget"
                                                   ".FrameLayout/android.widget.ScrollView/androidx.appcompat.widget"
                                                   ".LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat"
                                                   ".widget.LinearLayoutCompat/androidx.recyclerview.widget"
                                                   ".RecyclerView/android.view.ViewGroup[3]/android.widget.TextView[1]")
        self.SettingNotifyDesc = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                  "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                  ".widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                                  ".FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget"
                                                  ".LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget"
                                                  ".FrameLayout/android.widget.ScrollView/androidx.appcompat.widget"
                                                  ".LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat"
                                                  ".widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView"
                                                  "/android.view.ViewGroup[3]/android.widget.TextView[2]")
        self.SettingShowTitle = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                 "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                 ".widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                                 ".FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget"
                                                 ".LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget"
                                                 ".FrameLayout/android.widget.ScrollView/androidx.appcompat.widget"
                                                 ".LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat"
                                                 ".widget.LinearLayoutCompat/androidx.recyclerview.widget"
                                                 ".RecyclerView/android.view.ViewGroup[4]/android.widget.TextView[1]")
        self.SettingShowDesc = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                                ".widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                                ".FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget"
                                                ".LinearLayoutCompat/android.widget"
                                                ".FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView"
                                                "/androidx.appcompat.widget.LinearLayoutCompat/android.widget"
                                                ".ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx"
                                                ".recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android"
                                                ".widget.TextView[2]")
        self.SettingGeneralTitle = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".LinearLayout/android.widget.FrameLayout/android.widget"
                                                    ".FrameLayout/android.widget.FrameLayout/android.widget"
                                                    ".FrameLayout/androidx.appcompat.widget.LinearLayoutCompat"
                                                    "/android.widget.FrameLayout[1]/android.widget.FrameLayout"
                                                    "/android.view.ViewGroup/androidx.appcompat.widget"
                                                    ".LinearLayoutCompat/androidx.recyclerview.widget"
                                                    ".RecyclerView/android.widget.TextView[2]")
        self.SettingUpdateTitle = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                                   "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[5]/android.widget.TextView[1]")
        self.SettingUpdateDesc = (AppiumBy.XPATH,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.widget.TextView[2]")
        self.BluClubTitle = (AppiumBy.XPATH,
                             "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView[1]")
        self.BluClubDesc = (AppiumBy.XPATH,
                            "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]/android.widget.TextView[2]")
        self.SettingSupportTitle = (AppiumBy.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.TextView[1]")
        self.SettingSupportDesc = (AppiumBy.XPATH,
                                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[7]/android.widget.TextView[2]")
        self.SettingReferralTitle = (AppiumBy.XPATH,
                                     "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[8]/android.widget.TextView[1]")
        self.SettingReferralDesc = (AppiumBy.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[8]/android.widget.TextView[2]")
        self.SettingTermsTitle = (AppiumBy.XPATH,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[9]/android.widget.TextView[1]")
        self.SettingTermsDesc = (AppiumBy.XPATH,
                                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.appcompat.widget.LinearLayoutCompat/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/android.widget.ScrollView/androidx.appcompat.widget.LinearLayoutCompat/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[9]/android.widget.TextView[2]")
        self.SettingVersion = (AppiumBy.ID, "com.samanpr.blu.dev:id/versionTextView")
        self.SettingMadInIran = (AppiumBy.ID, "com.samanpr.blu.dev:id/madeInTextView")
        self.SettingGeneralTittle = (AppiumBy.ID, "com.samanpr.blu.dev:id/headerTitleTextView")

    def is_page_displayed(self):
        """بررسی اینکه صفحه تنظیمات نمایش داده شده است یا خیر"""
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.SettingTitle)
        )
        return self.driver.find_element(*self.SettingTitle).is_displayed()

    # مثال‌هایی از چگونگی استفاده از المان‌های دیگر
    def get_user_name(self):
        """دریافت نام کاربر"""
        return self.driver.find_element(*self.UserName).text

    def get_phone_number(self):
        """دریافت شماره تلفن کاربر"""
        return self.driver.find_element(*self.PhoneNumber).text

    def click_share_button(self):
        """کلیک روی دکمه اشتراک‌گذاری"""
        self.driver.find_element(*self.ShareButton).click()
