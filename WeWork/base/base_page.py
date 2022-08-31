"""
Name : base_page.py
Author  : Tiffany
Time : 2022/8/30 18:18
DESC: 
"""
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException

from WeWork.utils.log_utils import logger


class BasePage:
    def setup(self):
        # 资源初始化
        # 打开【企业微信】应用
        caps = {
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "deviceName": "127.0.0.1:7555",
            "noReset": "true"
        }
        # 创建driver, 与appium server 建立连接，返回一个session
        # driver变成self.driver 由局部变量变成实例变量，可以在其他的方法中引用这个实例变量
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(30)

    def teardown(self):
        self.driver.quit()

    def swipe_find(self, text, num=3):
        # 自定义滑动查找
        for i in range(num):
            try:
                ele = self.driver.find_element(AppiumBy.XPATH, f"//*[@text='{text}']")
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
