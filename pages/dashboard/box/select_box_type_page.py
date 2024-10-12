# pages/select_box_type_page.py
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.dashboard.box.box_profile_page import BoxProfilePage
from pages.dashboard.box.select_box_name_page import CreateBoxPage


class SelectBoxTypePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # XPathها و متن‌های اصلاح‌شده بر اساس اطلاعات جدید
        self.normal_box_button = (
        AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.samanpr.blu.dev:id/wealthBoxType'])[1]")
        self.normal_box_title = (AppiumBy.XPATH,
                                 "//android.widget.TextView[@resource-id='com.samanpr.blu.dev:id/titleTextView' and "
                                 "@text='بلوباکس']")
        self.normal_box_description = (AppiumBy.XPATH,
                                       "//android.widget.TextView["
                                       "@resource-id='com.samanpr.blu.dev:id/descriptionTextView' and @text='فضایی "
                                       "برای پس‌انداز هدفمند یا مدیریت مخارج با سود کوتاه‌مدت']")
        self.long_term_box_button = (
        AppiumBy.XPATH, "(//android.view.ViewGroup[@resource-id='com.samanpr.blu.dev:id/wealthBoxType'])[2]")
        self.long_term_box_title = (AppiumBy.XPATH,
                                    "//android.widget.TextView[@resource-id='com.samanpr.blu.dev:id/titleTextView' "
                                    "and @text='بیگ‌باکس']")
        self.long_term_box_description = (AppiumBy.XPATH,
                                          "//android.widget.TextView["
                                          "@resource-id='com.samanpr.blu.dev:id/descriptionTextView' and @text='فضایی "
                                          "برای سپرده‌گذاری بلندمدت تا ۲۲ درصد سود به صورت سالیانه']")
        self.page_select_type_title = (AppiumBy.XPATH,
                                       "//android.widget.TextView["
                                       "@resource-id='com.samanpr.blu.dev:id/descriptionTextView' and @text='نوع باکس "
                                       "خود را انتخاب کنید']")

    def select_normal_box(self):
        # انتخاب گزینه "باکس عادی"
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.normal_box_button)
        ).click()
        # هدایت به صفحه وارد کردن جزئیات باکس
        return CreateBoxPage(self.driver)

    def select_long_term_box(self):
        # انتخاب گزینه "باکس بلند مدت"
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.long_term_box_button)
        ).click()
        # هدایت به صفحه وارد کردن جزئیات باکس
        return BoxProfilePage(self.driver)

    def is_page_displayed(self):
        # بررسی نمایش صفحه انتخاب نوع باکس
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.page_select_type_title)
        )
        return self.driver.find_element(*self.page_select_type_title).is_displayed()

    def is_normal_box_title_correct(self):
        # بررسی عنوان "بلوباکس"
        return self.driver.find_element(*self.normal_box_title).text == "بلوباکس"

    def is_normal_box_description_correct(self):
        # بررسی توضیحات "باکس عادی"
        return self.driver.find_element(
            *self.normal_box_description).text == "فضایی برای پس‌انداز هدفمند یا مدیریت مخارج با سود کوتاه‌مدت"

    def is_long_term_box_title_correct(self):
        # بررسی عنوان "بیگ‌باکس"
        return self.driver.find_element(*self.long_term_box_title).text == "بیگ‌باکس"

    def is_long_term_box_description_correct(self):
        # بررسی توضیحات "باکس بلند مدت"
        return self.driver.find_element(
            *self.long_term_box_description).text == "فضایی برای سپرده‌گذاری بلندمدت تا ۲۲ درصد سود به صورت سالیانه"
