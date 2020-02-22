from asyncio import sleep

from selenium.webdriver.common.by import By

from page.base_page import BasePage


class MediaCatalog(BasePage):

    def upload_image(self, image_path):
        image_locator = (By.CSS_SELECTOR, '.ww_icon_GrayPic')
        add_image_locator = (By.CSS_SELECTOR, '.js_upload_file_selector')
        upload_image = (By.NAME, 'uploadImageFile')
        submit_button = (By.LINK_TEXT, '完成')

        self.find(image_locator).click()
        self.find(add_image_locator).click()
        self.find(upload_image).send_keys(image_path)
        sleep(3)
        self.find(submit_button).click()

