from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from page.base_page import BasePage
from page.edit_member import EditMember


class Contact(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"

    def add_member(self, username, acctid, mobile, **data):
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        mobile_locator = (By.NAME, 'mobile')
        save_locator = (By.CSS_SELECTOR, '.js_btn_save')
        self.find(name_locator).send_keys(username)
        self.find(acctid_locator).send_keys(acctid)
        self.find(mobile_locator).send_keys(mobile)

        self.finds(save_locator)[0].click()

    def goto_member_detail_page(self, username=''):
        # TODO: 先进入成员详情页，然后直接从列表进入编辑
        table_locator = (By.CSS_SELECTOR, '.js_list')
        usernames_locator = (By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        td_status_locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_td_Status > a')

        self.wait(expected_conditions.visibility_of_element_located(table_locator))  # 等待列表加载
        tds = self.finds(usernames_locator)
        for i, td in enumerate(tds):
            if username == td.get_attribute('title'):
                td.click()

    def goto_edit_member_page_for_memberlist(self, username=''):
        #指定一个成员名称，然后直接从列表进入编辑
        table_locator = (By.CSS_SELECTOR, '.js_list')
        usernames_locator = (By.CSS_SELECTOR, '#member_list td:nth-child(2)')
        tr_locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_tr')
        td_status_locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_td_Status > a')
        smart_menu_a_locator = (By.CSS_SELECTOR, '.smart_menu_a')

        self.wait(expected_conditions.visibility_of_element_located(table_locator))  # 等待列表加载
        trs = self.finds(tr_locator)
        tds = self.finds(usernames_locator)
        for i, td in enumerate(tds):
            if username == td.get_attribute('title'):
                self.move_to(td)
                trs[i].find_element(*td_status_locator).click()
                self.wait(expected_conditions.visibility_of_element_located(smart_menu_a_locator))
                self.finds(smart_menu_a_locator)[0].click()
                break
        return EditMember(reuse=True)

def get_titles_in_list(self, username) -> list:
    td_locator = (By.CSS_SELECTOR, '.member_colRight_memberTable_td')
    tds = self.finds(td_locator)
    return list(map(lambda x: x.get_attribute('title'), tds))
