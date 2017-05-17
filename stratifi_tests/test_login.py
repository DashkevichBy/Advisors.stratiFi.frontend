import logging
import os

import pytest

from common import BaseTest
from pages.advisors_stratifi_pages.sign_in_page import SignInPage
from pages.advisors_stratifi_pages.stratifi_page import StratifiPage

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


class TestLogin(BaseTest):

    def test_login(self):
        mylogger.info('Trying to login')
        sign_in_page = SignInPage()
        sign_in_page.open()
        sign_in_page.enter_login('akhil@stratifi.com')
        sign_in_page.enter_password('Hell0w0rld123!')
        sign_in_page.press_sign_in()
        stratifi_page = StratifiPage()
        stratifi_page.check_if_page_is_loaded()
        # print('Successfully logged in: ' + str(stratifi_page.is_element_present('startAnalise', timeout=60)))


if __name__ == "__main__":
    mylogger.info(' About to start the tests ')
    pytest.main(args=['-s', os.path.abspath(__file__)])
    mylogger.info(' Done executing the tests ')
