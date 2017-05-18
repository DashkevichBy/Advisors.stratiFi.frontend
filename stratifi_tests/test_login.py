import logging
import os

import pytest

from common import BaseTest
from pages.advisors_stratifi_pages.sign_in_page import SignInPage
from pages.advisors_stratifi_pages.stratifi_page import StratifiPage

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


class TestLogin(BaseTest):
    stratifi_page = StratifiPage()
    sign_in_page = SignInPage()

    def test_login(self):
        self.sign_in_page.open()
        self.sign_in_page.enter_login('akhil@stratifi.com')
        self.sign_in_page.enter_password('Hell0w0rld123!')
        self.sign_in_page.press_sign_in()
        # self.stratifi_page.check_if_page_is_loaded()
        # print('Successfully logged in: ' + str(stratifi_page.is_element_present('startAnalise', timeout=60)))


if __name__ == "__main__":
    pytest.main()

