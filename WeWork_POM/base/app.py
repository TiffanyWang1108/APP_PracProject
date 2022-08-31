"""
Name : app.py
Author  : Tiffany
Time : 2022/8/31 14:32
DESC: 
"""
# 启动 关闭 重启
from appium import webdriver

from WeWork_POM.base.base_page import BasePage


class App(BasePage):
    implicity_wait_time = 80

    def start(self):
        # 启动
        # 资源初始化
        # 打开【企业微信】应用
        caps = {
            "platformName": "Android",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "deviceName": "127.0.0.1:7555",
            # 防清缓存
            "noReset": "true",
            # "dontStopAppOnReset": "true",
            # 动态页面等待0秒,再查找元素，默认十秒
            "settins[waitForIdleTimeout]": 0
        }
        # 创建driver, 与appium server 建立连接，返回一个session
        # driver变成self.driver 由局部变量变成实例变量，可以在其他的方法中引用这个实例变量
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(self.implicity_wait_time)
        # return 到当前页面
        return self

    def restart(self):
        pass

    def quit(self):
        self.driver.quit()

    def go_to_main(self):
        # 进入首页的入口
        from WeWork_POM.page.MainPage import MainPage
        return MainPage()
