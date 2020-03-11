from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebview:
    def setup(self):
        CAPS = {
            "deviceName": "ace",
            "automationName": "UiAutomator2",
            "platformName": "Android",
            "chromedriverExecutable": "C:/web/driver/2.20.exe",
            "appPackage": "com.xueqiu.android",
            "appActivity": ".view.WelcomeActivityAlias",
            "adbExecTimeout": 35000,
            "noReset": True,
        }

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", CAPS)
        self.driver.implicitly_wait(20)

    def test_webview(self):
        xueying_locator = (By.CSS_SELECTOR, '.trade_home_xueying_SJY')
        phone_locator = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        auto_code_locator = (By.CSS_SELECTOR, '[placeholder="请输入验证码"]')
        close_locator = (MobileBy.ID, "action_bar_close")

        exchange_locator = (MobileBy.XPATH, "//*[contains(@resource-id, 'tab_name') and @text='交易']")
        self.driver.find_element(*exchange_locator).click()
        # 切换到webview
        WebDriverWait(self.driver, 15).until(lambda x: len(self.driver.contexts) > 1)
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(*xueying_locator).click()
        WebDriverWait(self.driver, 15).until(lambda x: len(self.driver.window_handles) > 3)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(phone_locator))
        self.driver.find_element(*phone_locator).send_keys("15515155222")
        self.driver.find_element(*auto_code_locator).send_keys("1234")
        self.driver.find_element(By.CSS_SELECTOR, ".open_form-submit_1Ms").click()
        toast = self.driver.find_element(By.CSS_SELECTOR, ".Toast_toast_22U").text
        print(toast)
        # 切换回native
        self.driver.switch_to.context(self.driver.contexts[0])
        self.driver.find_element(*close_locator).click()


    def teardown(self):
        pass
        # driver.quit()
