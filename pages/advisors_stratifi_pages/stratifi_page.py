import unittest
from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage


class StratifiPage(AbstractBasePage, unittest.TestCase):
    startAnalise = Find(by=By.XPATH, value='.//*[text()="Start Analyzing Your Portfolios"]')
    goToPrismButton = Find(by=By.XPATH, value='.//*[text()="Go to PRISM"]')
    clientsButton = Find(by=By.XPATH, value='.//*[text()="Clients"]')
    validClient = Find(by=By.XPATH, value='.//*[text()="Beckert"]')
    profileDropDown = Find(by=By.XPATH, value='.//*[@id="dropdownUserExtra"]')
    proposalsMenuItem = Find(by=By.XPATH, value='.//*[@id="dropdownUserExtra"]/following::a[text()="Proposals"]')
    grayGenerateProposalsButton = Find(by=By.XPATH, value='.//*[text()="Generate Proposal"]')
    propGenHeader = Find(by=By.XPATH, value='.//*[text()="Client proposal generation"]')
    accountCheckBox = Find(by=By.XPATH, value='.//*[@class="c-indicator icon-checkmark"]')
    greenGenerateProposalButton = Find(by=By.XPATH, value='.//*[text()="Generate proposal"]')
    proposalHeader = Find(by=By.XPATH, value='.//*[text()="StratiFi analysis"]')
    prismButton = Find(by=By.XPATH, value='.//*[text()="PRISM"]')
    strategiesButton = Find(by=By.XPATH, value='.//*[text()="Strategies"]')
    returnEnhancement = Find(by=By.XPATH, value='.//*[text()="StratiFi Return Enhancement"]')
    analyzeButton = Find(by=By.XPATH, value='.//*[text()="Analyze Strategy"]')
    availableClient = Find(by=By.XPATH, value='.//*[text()="John Beckert"]')
    continueButton = Find(by=By.XPATH, value='.//*[text()="Continue"]')
    generateProposalPopUp = Find(by=By.XPATH, value='.//*[text()="Generate Proposal"]')
    portfoliosButton = Find(by=By.XPATH, value='.//*[text()="Portfolios"]')

    def __init__(self):
        AbstractBasePage.__init__(self, "https://advisors.stratifi.com/advisor/")

# --------------Clicks-----------------------

    def press_start_analise(self):
        self.startAnalise.click()

    def press_go_to_prism(self):
        self.goToPrismButton.click()

    def press_prism_button(self):
        self.prismButton.click()

    def press_client_button(self):
        self.clientsButton.click()

    def chose_valid_client(self):
        self.validClient.click()

    def open_profile_dropdown(self):
        self.profileDropDown.click()

    def chose_proposal_menu_item(self):
        self.proposalsMenuItem.click()

    def press_gray_propgen_button(self):
        self.grayGenerateProposalsButton.click()

    def chose_account(self):
        self.accountCheckBox.click()

    def press_green_propgen_button(self):
        self.greenGenerateProposalButton.click()

    def press_strategies_button(self):
        self.strategiesButton.click()

    def press_return_enhancement_button(self):
        self.returnEnhancement.click()

    def press_analyze_button(self):
        self.analyzeButton.click()

    def chose_available_client(self):
        self.availableClient.click()

    def press_continue_button(self):
        self.continueButton.click()

    def press_portfolio_button(self):
        self.portfoliosButton.click()

# ---------------Asserts-------------------------------

    # def check_if_page_is_loaded(self):
    #    # assert u"StratiFi" in self.get_title(), "Stratifi page was not loaded"
    #    assert self.is_element_present("startAnalise", timeout=10), "Client proposal generation screen was not shown"

    def check_if_the_page_was_loaded(self):
       assert self.custom_is_element_present(how=By.XPATH, what='.//*[text()="Start Analyzing Your Portfolios"]', timeout=20), "Unable to load the page"


    def check_if_propgen_screen_was_shown(self):
       assert self.is_element_present("propGenHeader", timeout=10), "Client proposal generation screen was not shown"

    def check_if_proposal_was_generated(self):
       assert self.is_element_present("proposalHeader", timeout=40), "Proposal was not generated"

    def check_if_generate_proposal_popup_is_shown(self):
       assert self.is_element_present("generateProposalPopUp", timeout=10), "Generate proposal pop up was not shown"



