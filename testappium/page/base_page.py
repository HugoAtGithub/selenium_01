import logging

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    logging.basicConfig(level=logging.INFO)
    _driver: WebDriver
    # 自动处理的弹窗黑名单
    _black_list = {'id/tv_agree': (MobileBy.ID, 'tv_agree'),
                   'id/image_cancel': (MobileBy.ID, 'image_cancel'),
                   'text="确定"': (MobileBy.XPATH, '//*[@text="确定"]'),
                   'text="下次再说"': (MobileBy.XPATH, '//*[@text="下次再说"]')
                   }
    _error_max = 3
    _error_count = 1
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
        logging.info(f"当前在 {self.__class__.__name__} 页")

    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        try:
            # 寻找控件
            return self._self_find(locator, value)
        except Exception as e:
            # 超过弹窗处理次数则直接跑普通 find_element
            if self._error_count >= self._error_max:
                self._error_count = 1  # 重置次数
                self._self_find(locator, value)

            logging.info("进入弹窗处理")
            self._handleAlert()
            self._error_count += 1
            return self.find(locator, value)

    def _self_find(self, locator, value: str = None) -> WebElement:
        return self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
            locator, value)

    def _handleAlert(self):
        page_source = self._driver.page_source
        # 对黑名单里的弹框进行处理
        for key, element in self._black_list.items():
            if key in page_source:
                logging.info(f'找到弹窗： {element}')
                self._driver.find_element(*element).click()

    # todo: 通用异常 通过装饰器让函数自动处理异常
    def find_and_get_text(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)

        try:
            # 寻找控件
            element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(
                locator, value)
            # 如果成功，清空错误计数
            self._error_count = 0
            return element.text
        # done:   self._error_count = 0
        except Exception as e:
            # 如果次数太多，就退出异常逻辑，直接报错
            if self._error_count > self._error_max:
                raise e
            # 记录一直异常的次数
            self._error_count += 1
            # 对黑名单里的弹框进行处理
            for element in self._black_list:
                logging.info(element)
                elements = self._driver.find_elements(*element)
                if len(elements) > 0:
                    elements[0].click()
                    # 继续寻找原来的正常控件
                    return self.find_and_get_text(locator, value)
            # 如果黑名单也没有，就报错
            logging.warn("black list no one found")
            raise e

            # return self.find(locator, value)

    def get_toast(self):
        return self.find(By.XPATH, "//*[@class='android.widget.Toast']").text

    def text(self, key):
        return (By.XPATH, "//*[@text='%s']" % key)

    def find_by_text(self, key):
        return self.find(self.text(key))

if __name__ == '__main__':
    for key, element in BasePage._black_list.items():
        logging.info(element)