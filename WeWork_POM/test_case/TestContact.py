"""
Name : TestContact.py
Author  : Tiffany
Time : 2022/8/31 14:48
DESC: 
"""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from WeWork_POM.base.app import App
from WeWork_POM.utils.ContactInfo import ContactInfo


class TestContact:
    def setup(self):
        self.app = App()
        # 定义实例变量
        self.main = self.app.start().go_to_main()

    def teardown(self):
        pass

    def test_add_contact(self):
        name = ContactInfo.get_name()
        phone = ContactInfo.get_phone()
        result = self.main.go_to_contactlist().click_add_member() \
            .click_addmember_manual().edit_member(name, phone).get_text()
        assert "添加成功" == result
        # self.driver.find_element(AppiumBy.XPATH, "//*[@text='通讯录']").click()

