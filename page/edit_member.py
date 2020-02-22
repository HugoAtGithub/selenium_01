from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
from page.base_page import BasePage
from page.member_detail import MemberDetail


class EditMember(BasePage):

    def __init__(self, driver: WebDriver = None, reuse=False):
        super().__init__(driver, reuse)
        form_locator = (By.CSS_SELECTOR, '.member_edit_formWrap')
        self.wait(expected_conditions.visibility_of_element_located(form_locator))

    def set_english_name(self, english_name):
        locator = (By.NAME, 'english_name')
        name_input = self.find(locator)
        name_input.clear()
        name_input.send_keys(english_name)

    def save(self):
        locator = (By.CSS_SELECTOR, '.js_save')
        self.finds(locator)[0].click()
        return MemberDetail(reuse=True)
