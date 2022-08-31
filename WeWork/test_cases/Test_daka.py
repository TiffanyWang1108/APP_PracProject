"""
Name : Test_daka.py
Author  : Tiffany
Time : 2022/8/30 18:22
DESC: 
"""
from appium.webdriver.common.appiumby import AppiumBy

from WeWork.base.base_page import BasePage


class TestWorkBench(BasePage):
    def test_daka(self):
        """
        进入【工作台页面】
        点击【打卡】
        选择【外出打卡】tab
        点击【第n次打卡】
        验证点：提示【外出打卡成功】
        :return:
        """
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='工作台']").click()
        self.swipe_find("打卡").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text, '次外出')]").click()
        # 断言 assert find...最后一步，进行倒数第二部的验证
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='外出打卡成功']")
