# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestSearch():
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["automationName"] = "UiAutomator2"
        caps["deviceName"] = "ace"
        caps["appPackage"] = "com.xueqiu.android"
        caps["appActivity"] = ".view.WelcomeActivityAlias"
        caps["unicodeKeyboard"] = "true"
        caps["resetKeyboard"] = "false"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_search_alibaba_hk_price(self):
        stock_locator = (MobileBy.XPATH, "//*[contains(@resource-id, 'title_container')]/*[@text='股票']")
        price_locator = (MobileBy.XPATH, "//*[@text='09988']/../../..//*[contains(@resource-id,'current_price')]")

        self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*stock_locator).click()
        price = self.driver.find_element(*price_locator).text
        assert float(price) > 100

    def test_self_select(self):
        search_input_locator = (MobileBy.ID, "com.xueqiu.android:id/search_input_text")
        follow_btn = (MobileBy.ID, "follow_btn")
        followed_btn = (MobileBy.ID, "followed_btn")

        stock_name = "阿里巴巴"
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_agree").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(*search_input_locator).send_keys(stock_name)
        self.driver.find_element(MobileBy.ID, "name").click()
        self.driver.find_element(*follow_btn).click()

        # 返回到首页
        if len(self.driver.find_elements(*search_input_locator)):
            self.driver.back()
        self.driver.back()
        # 重新搜索
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(*search_input_locator).send_keys(stock_name)
        self.driver.find_element(MobileBy.ID, "name").click()
        btn_text = self.driver.find_element(*followed_btn).get_attribute("text")
        assert "已添加" == btn_text


    def teardown(self):
        sleep(5)
        self.driver.quit()
