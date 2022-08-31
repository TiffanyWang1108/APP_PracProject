"""
Name : test_contact.py
Author  : Tiffany
Time : 2022/8/30 15:44
DESC: 
"""
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

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
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='手动输入添加']").click()
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[contains(@text,'手机')]/..//android.widget.EditText").send_keys(phone)
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='保存']").click()
        # 等待打印页面布局
        print(self.driver.page_source)
        # 获取toast
        result = self.driver.find_element(AppiumBy.XPATH, "//*[@class='android.widget.Toast']").text
        # assert断言
        assert result == "添加成功"

    def wait_text_show(self, text):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.text_to_be_present_in_element((AppiumBy.XPATH, f"//*[@text='{text}']")))

    def wait_disappear(self, locator):
        WebDriverWait(self.driver, 10).until_not(
            lambda x: x.find_element(*locator))

    def test_delcontact(self):
        """
        打开【企业微信】应用
        进入【通讯录】页面
        点击右上角搜索图标，进入搜索页面
        输入搜索内容（已添加的联系人姓名）
        点击展示的第一个联系人（有可能多个），进入联系人详情页面
        点击右上角三个点，进入个人信息页面
        点击【编辑成员】进入编辑成员页面
        点击【删除成员】并确定
        验证点：
            搜索结果页面联系人不存在
        :return:
        """
        del_contactname = "张洋"
        # 进入【通讯录】页面
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()
        # 点击搜索图标，进入搜索页面
        # 图标属性不固定，通过父节点或兄弟节点定位
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[@text='加加加']/../../../following-sibling::*/*[1]").click()
        # 输入搜索内容
        self.driver.find_element(AppiumBy.XPATH,
                                 "//*[@text='搜索']").send_keys(del_contactname)
        result = self.wait_text_show("联系人")
        print(result)
        # 无搜索结果
        if not result:
            pytest.xfail(f"无搜索结果:{del_contactname}")
        # 有搜索结果--》进行删除操作
        del_contact_locator = (AppiumBy.XPATH, f"//*[@text='联系人']/../following-sibling::*//*[@text={del_contactname}]")
        self.driver.find_element(*del_contact_locator).click()
        # 点击个人信息 ...
        InfoLocator = (AppiumBy.XPATH, "//*[@text='个人信息']/../../../../following-sibling::*[1]")
        self.driver.find_element(*InfoLocator).click()
        # 点击编辑成员
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='编辑成员']").click()
        # 滑动页面找到删除成员按钮
        self.swipe_find("删除成员").click()
        # 点击确定，删除成员
        self.driver.find_element(AppiumBy.XPATH, "//*[@text='确定']").click()
        # 验证结果
        # 等待某个元素消失,相当于断言
        self.wait_disappear(del_contact_locator)
