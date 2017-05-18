import time

import pytest
from pages.advisors_stratifi_pages.stratifi_page import StratifiPage

from common import BaseTest
from pages.advisors_stratifi_pages.risk_analysis_page import RiskAnalysisPage


class TestPropGenFromPrism(BaseTest):
    def xtest_propgen_from_prism(self):
        stratifi_page = StratifiPage()
        risk_analysis_page = RiskAnalysisPage()
        stratifi_page.open()
        stratifi_page.check_if_page_is_loaded()
        # print('Page is loaded: ' + str(stratifi_page.is_element_present('startAnalise')))
        stratifi_page.press_start_analise()
        stratifi_page.press_go_to_prism()
        risk_analysis_page.open_chose_module_dropdown()
        risk_analysis_page.select_first_option()
        risk_analysis_page.open_date_range_dropdown()
        risk_analysis_page.press_set_range_button()
        risk_analysis_page.check_prism_analysis_is_shown()
        # print('Prism from main page works: ' + str(risk_analysis_page.is_element_present('overviewForHeader', timeout=5)))
        time.sleep(5)
        risk_analysis_page.press_custom_overlay_button()
        risk_analysis_page.check_if_proposal_from_prism_generated()
        # print('Proposal from prism was successfully generated: ' + str(risk_analysis_page.is_element_present('summaryHeader', timeout=5)))


if __name__ == "__main__":
    pytest.main()
