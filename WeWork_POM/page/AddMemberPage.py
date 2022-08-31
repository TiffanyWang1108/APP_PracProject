"""
Name : AddMemberPage.py
Author  : Tiffany
Time : 2022/8/31 14:38
DESC: 
"""
from appium.webdriver.common.appiumby import AppiumBy

from WeWork_POM.base.base_page import BasePage


class AddMemberPage(BasePage):

    def click_addmember_manual(self):
        # 点击手动输入添加成员
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        from WeWork_POM.page.EditMemberPage import EditMemberPage
        return EditMemberPage(self.driver)

    def get_text(self):
        # 获取toast
        result = self.driver.find_element(AppiumBy.XPATH,
                                          "//*[@class='android.widget.Toast']").text
        return result
