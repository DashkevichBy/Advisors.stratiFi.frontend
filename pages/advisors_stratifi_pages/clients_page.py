from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage


class ClientsPage(AbstractBasePage):
    firstAccountsNotLinkedClient = Find(by=By.XPATH, value='(.//*[text()="Accounts not linked"])[2]')
    clientsHeader = Find(by=By.XPATH, value='.//h4[text()="Clients"]')

    def __init__(self):
            AbstractBasePage.__init__(self, "https://advisors.stratifi.com/advisor/investors")

    # ------------Clicks------------------------------

    def press_accnotlinked_button_on_first_available_client(self):
        self.firstAccountsNotLinkedClient.click()

    # ------------Send Keys------------------------------

    # ------------Asserts------------------------------
    def check_if_clients_page_is_opened(self):
        assert self.is_element_present("clientsHeader", timeout=60), "Unable to load Clients page"
