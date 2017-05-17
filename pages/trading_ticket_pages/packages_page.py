from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage


class PackagesPage(AbstractBasePage):
    packagesHeader = Find(by=By.XPATH, value='.//*[text()="Packages"]')
    createPackageButton = Find(by=By.XPATH, value='.//*[text()="Create a package"]')

    def __init__(self):
            AbstractBasePage.__init__(self, "http://operations.stratifi.com/packages")

    # ------------Clicks------------------------------

    def press_create_a_package(self):
        self.createPackageButton.click()

    # ------------Send Keys------------------------------

    # ---------------Asserts-------------------------------

    def check_if_trading_ticket_page_is_loaded(self):
       assert self.is_element_present("packagesHeader", timeout=10), "Packages page was not loaded"



