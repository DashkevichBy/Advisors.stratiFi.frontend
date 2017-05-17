from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage


class PackagesCreatePage(AbstractBasePage):
    createPackageHeader = Find(by=By.XPATH, value='.//*[text()="Create a Package"]')
    packageNameField = Find(by=By.XPATH, value='.//*[@name="description"]')
    templateDropdown = Find(by=By.XPATH, value='.//*[text()="Select template"]/parent::*')
    atLeastOneAccount = Find(by=By.XPATH, value='.//td[text()="1"]')
    firstStrategy = Find(by=By.XPATH, value='.//*[text()="StratiFi RE RR"]')




    def __init__(self):
        AbstractBasePage.__init__(self, "http://operations.stratifi.com/packages/create")

    # ------------Clicks------------------------------

    def select_the_first_strategy(self):
        self.firstStrategy.click()

    # ------------Send Keys------------------------------

    def enter_package_name(self, package_name):
        self.packageNameField.send_keys(package_name)

    # ---------------Asserts-------------------------------

    def check_if_there_is_at_least_one_account(self):
       assert self.is_element_present("atLeastOneAccount", timeout=60), "There are no accounts for selected strategy"

    def check_if_create_a_package_page_is_loaded(self):
       assert self.is_element_present("createPackageHeader", timeout=10), "Create package page was not loaded"


