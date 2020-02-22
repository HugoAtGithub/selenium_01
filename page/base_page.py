from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _base_url = ""
    _driver = None

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                options = webdriver.ChromeOptions()
                options.debugger_address = "127.0.0.1:9222"
                # options.add_argument("--window-size=1366,768")
                self._driver = webdriver.Chrome(options=options)
            else:
                # index 页面会使用这个
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(3)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    def close(self):
        sleep(10)
        self._driver.quit()

    def find(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    def finds(self, by, locator=""):
        if isinstance(by, tuple):
            return self._driver.find_elements(*by)
        else:
            return self._driver.find_elements(by, locator)

    def move_to(self, element):
        chains = ActionChains(self._driver)
        chains.move_to_element(element).perform()

    def wait(self, method, maxtime=10):
         return WebDriverWait(self._driver, maxtime).until(method)