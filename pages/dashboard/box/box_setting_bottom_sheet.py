from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BoxSettingBottomSheet(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.title = (AppiumBy.ID, "com.samanpr.blu.dev:id/titleTextView")
        self.description = (AppiumBy.ID, "com.samanpr.blu.dev:id/descriptionTextView")

        # دکمه‌ها
        self.edit_name_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className('
                                                               '"android.view.ViewGroup").instance(2)')
        self.delete_box_button_text = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("برداشت موجودی و حذف")')

        # دکمه‌های مربوط به حذف
        self.cancel_box_button = (AppiumBy.ID, 'com.samanpr.blu.dev:id/cancelButton')
        self.confirm_delete_button = (AppiumBy.ID, 'com.samanpr.blu.dev:id/confirmButton')

    def click_edit_name(self):
        """کلیک روی دکمه ویرایش نام و هدایت به صفحه تغییر نام باکس"""
        from pages.dashboard.box.select_box_name_page import CreateBoxPage  # وارد کردن داخل متد
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.edit_name_button)
        ).click()
        return CreateBoxPage(self.driver)  # هدایت به صفحه ویرایش نام باکس

    def click_delete_box(self):
        """کلیک روی دکمه حذف باکس و باز کردن مودال تأیید حذف"""
        from pages.dashboard.box.box_confirm_modal import BoxConfirmModal  # وارد کردن داخل متد
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.delete_box_button_text)
        ).click()
        return BoxConfirmModal(self.driver)  # باز کردن مودال تأیید حذف
