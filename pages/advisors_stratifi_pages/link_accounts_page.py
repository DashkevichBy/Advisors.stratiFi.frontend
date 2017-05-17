from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage
from random import randint
from webium.controls.select import Select
import unittest


class LinkAccountsPage(AbstractBasePage, unittest.TestCase):
    linkAccountsHeader = Find(by=By.XPATH, value='.//*[contains(text(),"Link accounts to ")]')
    addAccountButton = Find(by=By.XPATH, value='.//*[@class = "btn btn-primary btn-round"]')
    createAnAccountButton = Find(by=By.XPATH, value='.//*[text()="Create an account"]')
    accTypeDropdown = Find(by=By.XPATH, value='.//*[text()="Select account type"]/parent::*')
    custodianDropdown = Find(by=By.XPATH, value='.//*[@name="custodian"]')
    firstCustodianOption = Find(Select, By.XPATH, '(.//*[@name="custodian"]/child::*)[2]')
    # firstCustodianOption = Find(by=By.XPATH, value='(.//*[@name="custodian"]/child::*)[2]')
    accNameField = Find(by=By.XPATH, value='.//*[@name="name"]')
    accNumber = Find(by=By.XPATH, value='.//*[@name="number"]')
    createButton = Find(by=By.XPATH, value='.//*[text()="Create"]')
    addedAutotestAccount = Find(by=By.XPATH, value='.//*[@class = "table table-bordered table-split"]/descendant::*[contains(text(),"Autotest account")]')
    firstAccType = Find(by=By.XPATH, value='(.//*[text()="Select account type"]/following-sibling::*)[1]')
    docTypeDropdown = Find(by=By.XPATH, value='.//*[text()="Select document type"]/parent::*')
    firstDocType = Find(by=By.XPATH, value='(.//*[text()="Select document type"]/following-sibling::*)[1]')
    nextButton = Find(by=By.XPATH, value='.//*[text()="Next"]')
    unlinkAccButton = Find(by=By.XPATH, value='.//*[@class="btn btn-grey btn-round"]')

    # select = Select(custodianDropdown)

    def __init__(self):
            AbstractBasePage.__init__(self, "https://advisors.stratifi.com/advisor/investors/17/link-accounts")

    # ------------Clicks------------------------------

    def press_add_account_button(self):
        self.addAccountButton.click()

    def open_acc_type_dropdown(self):
        self.accTypeDropdown.click()

    def open_custodian_dropdown(self):
        self.custodianDropdown.click()

    def select_first_custodian_option(self):
        self.firstCustodianOption.click()

    def press_create_button(self):
        self.createButton.click()

    def select_first_acc_type(self):
        self.firstAccType.click()

    def open_doc_type_dropdown(self):
        self.docTypeDropdown.click()

    def select_first_doc_type(self):
        self.firstDocType.click()

    def press_next_button(self):
        self.nextButton.click()

    def press_create_an_account_button(self):
        self.createAnAccountButton.click()

    def press_unlink_acc_button(self):
        self.unlinkAccButton.click()

    # ------------Send Keys------------------------------

    def enter_account_name(self, name):
        self.accNameField.send_keys(name)

    def enter_random_acc_number(self):
        self.accNumber.send_keys(str(randint(100000000000, 999999999999)))

    # ------------Asserts------------------------------
    def check_if_link_accounts_page_is_opened(self):
        assert self.is_element_present("linkAccountsHeader", timeout=60), "Unable to load Link Accounts page"

    def check_if_new_account_was_added(self):
        assert self.is_element_present("addedAutotestAccount", timeout=10), "Autotest account wasn't added"

    def check_if_target_account_was_deleted(self):
        self.assertFalse(self.is_element_present("unlinkAccButton", timeout=5), "Target account was not deleted")
