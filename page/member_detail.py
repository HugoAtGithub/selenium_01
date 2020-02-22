from selenium.webdriver.common.by import By

from page.base_page import BasePage


class MemberDetail(BasePage):
    def get_english_name(self):
        locator = (By.CSS_SELECTOR, '.member_display_cover_detail_bottom')
        text = self.finds(locator)[0].text
        content = str(text) if text else ''
        return content