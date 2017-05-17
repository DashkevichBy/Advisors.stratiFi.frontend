import time

import pytest
from pages.advisors_stratifi_pages.risk_analysis_page import RiskAnalysisPage
from pages.advisors_stratifi_pages.stratifi_page import StratifiPage

from common import BaseTest
from pages.advisors_stratifi_pages.models_page import ModelsPage


class TestPrism(BaseTest):
    def test_prism_from_dashboard(self):
        stratifi_page = StratifiPage()
        stratifi_page.check_if_page_is_loaded()
        print('Page is loaded: ' + str(stratifi_page.is_element_present('startAnalise')))
        stratifi_page.press_start_analise()
        stratifi_page.press_go_to_prism()
        risk_analysis_page = RiskAnalysisPage()
        risk_analysis_page.open_chose_module_dropdown()
        risk_analysis_page.select_first_option()
        risk_analysis_page.open_date_range_dropdown()
        risk_analysis_page.press_set_range_button()

        risk_analysis_page.check_prism_analysis_is_shown()
        print('Prism from dashboard works: ' + str(risk_analysis_page.is_element_present('overviewForHeader')))

    def test_prism_from_left_panel(self):
        stratifi_page = StratifiPage()
        stratifi_page.open()
        stratifi_page.press_prism_button()
        stratifi_page.press_go_to_prism()
        risk_analysis_page = RiskAnalysisPage()
        risk_analysis_page.open_chose_module_dropdown()
        risk_analysis_page.select_first_option()
        risk_analysis_page.open_date_range_dropdown()
        risk_analysis_page.press_set_range_button()
        risk_analysis_page.check_prism_analysis_is_shown()
        print('Prism from left panel: ' + str(risk_analysis_page.is_element_present('overviewForHeader')))

    def test_prism_creating_new_model(self):
        stratifi_page = StratifiPage()
        stratifi_page.open()
        stratifi_page.press_prism_button()
        stratifi_page.press_go_to_prism()
        risk_analysis_page = RiskAnalysisPage()
        risk_analysis_page.press_add_models_button()
        risk_analysis_page.check_if_model_portfolio_screen_is_shown()
        print('Create Model Portfolio screen opened: ' + str(risk_analysis_page.is_element_present('modelNameField')))
        risk_analysis_page.enter_model_name("Model for autotest")
        risk_analysis_page.open_model_type_dropdown()
        risk_analysis_page.chose_model_type_conservative()
        risk_analysis_page.enter_a_ticker("AAC")
        risk_analysis_page.check_if_any_tickers_suggested()
        risk_analysis_page.chose_first_suggestion()
        risk_analysis_page.enter_model_weight("100")
        risk_analysis_page.press_create_model_button()
        risk_analysis_page.check_if_new_model_was_saved()
        time.sleep(2)
        risk_analysis_page.open_date_range_dropdown()
        risk_analysis_page.press_set_range_button()
        risk_analysis_page.check_prism_analysis_is_shown()
        print('Prism analysis for new model works: ' + str(risk_analysis_page.is_element_present('overviewForHeader')))

    def test_archive_created_model(self):
        stratifi_page = StratifiPage()
        stratifi_page.open()
        stratifi_page.press_portfolio_button()
        models_page = ModelsPage()
        models_page.check_models_page_loaded()
        models_page.check_if_created_model_is_in_the_list()
        models_page.press_archive_button_for_target_model()
        time.sleep(3)
        models_page.check_if_target_model_was_deleted()
        print('The model was not archived: ' + str(models_page.is_element_present('targetModel')))

if __name__ == "__main__":
    pytest.main()
