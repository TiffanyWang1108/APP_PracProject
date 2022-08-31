"""
Name : EditMemberPage.py
Author  : Tiffany
Time : 2022/8/31 14:42
DESC: 
"""
from appium.webdriver.common.appiumby import AppiumBy

from WeWork_POM.base.base_page import BasePage


class EditMemberPage(BasePage):

    def edit_member(self, name, phone):
        # 输入姓名
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        # 输入手机号
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phone)
        # 点击保存按钮
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        from WeWork_POM.page.AddMemberPage import AddMemberPage
        return AddMemberPage(self.driver)
