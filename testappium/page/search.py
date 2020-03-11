from appium.webdriver.common.mobileby import MobileBy

from testappium.page.base_page import BasePage


class Search(BasePage):
    def search(self, key = ""):
        search_locator = (MobileBy.ID, "search_input_text")
        name_locator = (MobileBy.ID, "name")
        self.find(search_locator).send_keys(key)
        self.find(name_locator).click()
        return self

    def add_select(self):
        add_locator = (MobileBy.ID, "follow_btn")
        self.find(add_locator).click()
        return self


    def close_page(self):
        close_locator = (MobileBy.ID, "action_close")
        self.find(close_locator).click()
