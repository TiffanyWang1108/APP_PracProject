"""
Name : test_contact.py
Author  : Tiffany
Time : 2022/8/30 15:44
DESC: 
"""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from WeWork.base.base_page import BasePage
from WeWork.utils.ContactInfo import ContactInfo
from WeWork.utils.log_utils import logger


class TestContact(BasePage):

    def test_contact(self):
        """
        通讯录添加成员用例步骤

            # 进入【通讯录】页面
            点击【添加成员】
            点击【手动输入添加】
            输入【姓名】【手机号】并点击【保存】
        验证点：
            登录成功提示信息
        """
        name = ContactInfo.get_name()
        phone = ContactInfo.get_phone()
        # 进入【通讯录】页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # 点击【添加成员】
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='添加成员']").click()
        # 滑动页面找到  添加成员 并点击
        self.swipe_find("添加成员").click()
        # 点击手动输入添加
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动出入添加']").click()
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'姓名')]/..//android.widget.EditText").send_keys(phone)
        self.driver.find_element(AppiumBy.XPATH, "com.tencent.wework:id/at6").click()
        # 等待打印页面布局
        print(self.driver.page_source)
        # 获取toast
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        # assert断言
        assert result == "添加成功"
