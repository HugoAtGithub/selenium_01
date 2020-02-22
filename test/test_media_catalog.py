from page.manage_tools import ManageTools


class TestMediaCatalog():

    def test_upload_image(self):
        managetoolsPage = ManageTools(reuse=True)
        mcPage = managetoolsPage.goto_media_catalog_page()
        mcPage.upload_image('D:/Pictures/1420446370567146.jpg')
