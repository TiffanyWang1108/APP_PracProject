"""
Name : base_page.py
Author  : Tiffany
Time : 2022/8/31 15:16
DESC: 
"""
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException

from WeWork_POM.utils.log_utils import logger


class BasePage:
    implicity_wait_time = 30

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find(self, by, locator):
        return self.driver.find_elements(by, locator)

    def set_implicity(self,second):
        self.driver.implicitly_wait(second)

    def swipe_find(self, text, num=3):
        # 自定义滑动查找
        # self.driver.implicitly_wait(2)
        self.set_implicity(1)
        for i in range(num):
            try:
                ele = self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{text}']")
                self.driver.implicitly_wait(self.implicity_wait_time)
                return ele
            except:
                logger.info("未找到元素，开始滑动")
                # 获取当前屏幕尺寸
                size = self.driver.get_window_size()
                width = size.get("width")
                height = size.get("height")
                logger.info(f"当前屏幕的宽:{width}, 高：{height}")
                start_x = width / 2
                start_y = height * 0.8
                end_x = width / 2
                end_y = height * 0.3
                duration = 2500
                self.driver.swipe(start_x, start_y, end_x, end_y, duration)
            if i == num - 1:
                raise NoSuchElementException(f"找了{num}次，未找到元素{text}")
