from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from page.base_page import BasePage
from page.edit_member import EditMember
from page.media_catalog import MediaCatalog


class ManageTools(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#manageTools"

    def goto_media_catalog_page(self) -> MediaCatalog:
        mc_locator = (By.CSS_SELECTOR, '[href="#material/text"]')
        self.wait(expected_conditions.element_to_be_clickable(mc_locator))
        self.find(mc_locator).click()
        return MediaCatalog(reuse=True)