"""
Name : MainPage.py
Author  : Tiffany
Time : 2022/8/31 14:34
DESC: 
"""
import time

from appium.webdriver.common.appiumby import AppiumBy

from WeWork_POM.base.base_page import BasePage


class MainPage(BasePage):

    def go_to_contactlist(self):
        # click 通讯录
        time.sleep(15)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        from WeWork_POM.page.ContactlistPage import ContactlistPage
        return ContactlistPage(self.driver)
