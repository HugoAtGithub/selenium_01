# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from testappium.page.app import App


class TestMarket():
    def setup(self):
        self.main = App().start().main()


    def test_self_select(self):
        search_page = self.main.goto_market_page().goto_search()
        search_page.search('alibaba').add_select().close_page()
