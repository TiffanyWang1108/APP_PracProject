"""
Name : ContactlistPage.py
Author  : Tiffany
Time : 2022/8/31 14:36
DESC: 
"""
from WeWork_POM.base.base_page import BasePage


class ContactlistPage(BasePage):

    def click_add_member(self):
        # 点击添加成员按钮
        self.swipe_find("添加成员").click()
        from WeWork_POM.page.AddMemberPage import AddMemberPage
        return AddMemberPage(self.driver)
