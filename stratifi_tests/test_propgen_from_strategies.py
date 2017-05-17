import time

import pytest
from common import Driver
from common import BaseTest
from pages.advisors_stratifi_pages.stratifi_page import StratifiPage


class TestPropGenFromStrategies(BaseTest):
    def test_propgen_from_strategies(self):
        stratifi_page = StratifiPage()
        stratifi_page.open()
        stratifi_page.check_if_page_is_loaded()
        # print('Page is loaded: ' + str(stratifi_page.is_element_present('startAnalise')))
        stratifi_page.press_strategies_button()
        stratifi_page.press_return_enhancement_button()
        stratifi_page.press_analyze_button()
        stratifi_page.check_if_generate_proposal_popup_is_shown()
        # print('Generate Proposal pop up is shown: ' + str(stratifi_page.is_element_present('generateProposalPopUp')))
        stratifi_page.chose_available_client()
        stratifi_page.press_continue_button()
        stratifi_page.check_if_propgen_screen_was_shown()
        # print('Client proposal generation is opened: ' + str(stratifi_page.is_element_present('propGenHeader')))
        stratifi_page.chose_account()
        time.sleep(2)
        stratifi_page.press_green_propgen_button()
        stratifi_page.check_if_proposal_was_generated()
        # print('Proposal was generated: ' + str(stratifi_page.is_element_present('proposalHeader')))
        Driver.get().close()


if __name__ == "__main__":
    pytest.main()

