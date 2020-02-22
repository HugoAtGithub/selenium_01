from time import sleep

from page.contact import Contact


class TestContact():

    def test_add_member(self):
        pass

    def test_edit_member(self):
        contactPage = Contact(reuse=True)
        editMemberPage = contactPage.goto_edit_member_page_for_memberlist('test1')
        editMemberPage.set_english_name('haha')
        memberDetailPage = editMemberPage.save()
        assert 'haha' in memberDetailPage.get_english_name()
