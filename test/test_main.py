import random
import time

import pytest

from page.main import Main


class TestMain():
    def setup(self):
        self.main = Main(reuse=True)

    @pytest.mark.parametrize("username, mobile",
                             [('test', '15515155166')])
    def test_add_member(self, username, mobile):
        t = str(int(time.time()))
        username += t
        contactPage = self.main.goto_add_member()
        contactPage.add_member(username, t, mobile)

        titles = contactPage.get_titles_in_list(username)
        assert username in titles

    def teardown(self):
        self.main.close()