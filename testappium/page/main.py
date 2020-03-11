from appium.webdriver.common.mobileby import MobileBy

from testappium.page.base_page import BasePage
from testappium.page.market import Market


class Main(BasePage):
    def goto_market_page(self):
        market_locator = (MobileBy.XPATH, "//*[contains(@resource-id, 'tab_name') and @text='行情']")
        self.find(market_locator).click()
        return Market(self._driver)


