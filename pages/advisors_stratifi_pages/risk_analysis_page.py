from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage


class RiskAnalysisPage(AbstractBasePage):
    overviewForHeader = Find(by=By.XPATH, value='.//*[contains(text(),"PRISM Overview for")]')
    viewCustomOverlayButton = Find(by=By.XPATH, value='.//*[text()="View a custom stratifi overlay"]')
    summaryHeader = Find(by=By.XPATH, value='.//*[text()="Summary"]')
    progressBar = Find(by=By.XPATH, value='.//*[@class="loader-items flex justify-center"]')
    firstOptionInDropDown = Find(by=By.XPATH, value='.//*[text()="Created Models"]/following::li[1]')
    dateRangeButton = Find(by=By.XPATH, value='.//*[text()="Select a date range"]')
    choseModelButton = Find(by=By.XPATH, value='.//*[text()="Use your model or single stock"]')
    addModelsButton = Find(by=By.XPATH, value='.//*[contains(text(),"Add models")]')
    modelNameField = Find(by=By.XPATH, value='.//*[@name = "name"]')
    modelTypeConservative = Find(by=By.XPATH, value='.//*[text()="Conservative"]')
    tickerField = Find(by=By.XPATH, value='.//*[@placeholder = "Enter a ticker."]')
    modelWeight = Find(by=By.XPATH, value='.//*[@placeholder = "Value"]')
    createModelButton = Find(by=By.XPATH, value='.//*[text()="Create model"]')
    firstSuggestion = Find(by=By.XPATH, value='.//*[@data-suggestion-index = "0"]')
    createdModelName = Find(by=By.XPATH, value='.//*[@data-suggestion-index = "0"]')
    correctNameOfNewModel = Find(by=By.XPATH, value='.//button/descendant::span[text()="Model for autotest"]')
    setRangeButton = Find(by=By.XPATH, value='.//*[text()="Set range"]')
    openModelTypeDropdown = Find(by=By.XPATH, value='.//*[@type="button" and @data-toggle="dropdown"]')

    def __init__(self):
            AbstractBasePage.__init__(self, "https://advisors.stratifi.com/advisor/risk-analysis")

    # ------------Clicks------------------------------

    def press_custom_overlay_button(self):
        self.viewCustomOverlayButton.click()

    def select_first_option(self):
        self.firstOptionInDropDown.click()

    def open_chose_module_dropdown(self):
        self.choseModelButton.click()

    def open_date_range_dropdown(self):
        self.dateRangeButton.click()

    def press_add_models_button(self):
        self.addModelsButton.click()

    def chose_model_type_conservative(self):
        self.modelTypeConservative.click()

    def press_create_model_button(self):
        self.createModelButton.click()

    def chose_first_suggestion(self):
        self.firstSuggestion.click()

    def open_model_type_dropdown(self):
        self.openModelTypeDropdown.click()

    def press_set_range_button(self):
        self.setRangeButton.click()

    # ------------Send Keys------------------------------

    def enter_a_ticker(self, ticker):
        self.tickerField.send_keys(ticker)

    def enter_model_weight(self, model_weight):
        self.modelWeight.send_keys(model_weight)

    def enter_model_name(self, model_name):
        self.modelNameField.send_keys(model_name)

    # ------------Asserts------------------------------

    def check_if_new_model_was_saved(self):
        assert self.is_element_present("correctNameOfNewModel", timeout=5), "New Model name is incorrect or something went wrong"

    def check_if_any_tickers_suggested(self):
        assert self.is_element_present("firstSuggestion", timeout=60), "I can't see any suggested tickers"

    def check_prism_analysis_is_shown(self):
        assert self.is_element_present("overviewForHeader", timeout=60), "Prism analysis was not shown"

    def check_if_proposal_from_prism_generated(self):
        assert self.is_element_present("summaryHeader", timeout=60), "Proposal from prism was not generated"

    def check_if_model_portfolio_screen_is_shown(self):
        assert self.is_element_present("modelNameField", timeout=60), "Prism analysis was not shown"





