import time

import pytest

from common import BaseTest
from pages.advisors_stratifi_pages.stratifi_page import StratifiPage


class TestPropGenFromClients(BaseTest):
    def test_propgen_from_clientlist(self):
        stratifi_page = StratifiPage()
        stratifi_page.open()
        stratifi_page.check_if_page_is_loaded()
        # print('Page is loaded: ' + str(stratifi_page.is_element_present('clientsButton')))
        stratifi_page.press_client_button()
        stratifi_page.chose_valid_client()
        stratifi_page.open_profile_dropdown()
        stratifi_page.chose_proposal_menu_item()
        stratifi_page.press_gray_propgen_button()
        stratifi_page.check_if_propgen_screen_was_shown()
        # print('Client proposal generation screen is opened: ' + str(stratifi_page.is_element_present('propGenHeader')))
        stratifi_page.chose_account()
        time.sleep(2)
        stratifi_page.press_green_propgen_button()
        stratifi_page.check_if_proposal_was_generated()
        # print('Proposal was generated: ' + str(stratifi_page.is_element_present('proposalHeader')))


if __name__ == "__main__":
    pytest.main()
