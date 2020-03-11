import datetime
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from testappium.page.base_page import BasePage
from testappium.page.main import Main


class App(BasePage):
    _package = "com.xueqiu.android"
    _activity = ".view.WelcomeActivityAlias"

    def start(self):
        # 启动app首页，复用driver直接跳转首页activity
        if self._driver is None:
            caps = {}
            caps["platformName"] = "Android"
            caps["automationName"] = "UiAutomator2"
            caps["deviceName"] = "ace"
            caps["appPackage"] = self._package
            caps["appActivity"] = self._activity
            # caps["noReset"] = True
            # caps["unicodeKeyboard"] = "true"
            # caps["resetKeyboard"] = "false"

            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(self._package, self._activity)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        def wait_load(driver):
            print(datetime.datetime.now())
            source = self._driver.page_source

            if "我的" in source:
                return True
            if "同意" in source:
                return True
            if "image_cancel" in source:
                return True
            return False
        WebDriverWait(self._driver, 60).until(wait_load)
        return Main(self._driver)