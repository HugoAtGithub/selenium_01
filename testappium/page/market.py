from appium.webdriver.common.mobileby import MobileBy

from testappium.page.base_page import BasePage
from testappium.page.search import Search


class Market(BasePage):
    def goto_search(self):
        search_locator = (MobileBy.ID, "action_search")
        self.find(search_locator).click()
        return Search(self._driver)

