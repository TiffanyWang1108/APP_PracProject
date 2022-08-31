"""
Name : test_delete.py
Author  : Tiffany
Time : 2022/8/31 10:35
DESC: 
"""
from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from WeWork.base.base_page import BasePage


class TestDelete(BasePage):
    def test_delete(self):
        """
        点击通讯录
        点击 需要删除的成员
        点击【更多】
        点击编辑成员
        滑动页面 & 点击删除成员
        toast提示点击确定
        验证点：
            判断成员名称是否删除
        :return:
        """
        # 点击通讯录
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='张勇']").click()
        self.driver.find_element(AppiumBy.ID, "com.tencent.wework:id/izx").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='编辑成员']").click()
        self.swipe_find("删除成员").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='确定']").click()
        sleep(10)


