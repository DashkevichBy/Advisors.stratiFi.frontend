from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage
import unittest


class DocumentsPage(AbstractBasePage, unittest.TestCase):
    reviewDocumentsHeader = Find(by=By.XPATH, value='.//*[@class="container"]/child::*[text()="Review Documents"]')
    markAsSubmittedFirst = Find(by=By.XPATH, value='(.//*[text()="Mark as submitted"])[1]')
    markAsSubmittedSecond = Find(by=By.XPATH, value='(.//*[text()="Mark as submitted"])[2]')
    markAsSubmittedThird = Find(by=By.XPATH, value='(.//*[text()="Mark as submitted"])[3]')
    sendButton = Find(by=By.XPATH, value='.//*[text()="Send"]')
    almostThereHeader = Find(by=By.XPATH, value='.//*[text()="Almost there!"]')
    sendButtonOnAlmostThereScreen = Find(by=By.XPATH, value='.//*[text()="Almost there!"]/following::*[text()="Send"]')
    congrats = Find(by=By.XPATH, value='.//*[text()="Congratulations!"]')
    okButton = Find(by=By.XPATH, value='.//*[text()="OK"]')
    linkAccBreadCrumb = Find(by=By.XPATH, value='.//*[text()="Link Accounts"]')

    def __init__(self):
        AbstractBasePage.__init__(self, "https://advisors.stratifi.com/advisor/investors/17/documents")

# --------------Clicks-----------------------

    def mark_all_documents_as_signed(self):
        self.markAsSubmittedFirst.click()
        self.markAsSubmittedSecond.click()
        self.markAsSubmittedThird.click()

    def press_send_button(self):
        self.sendButton.click()

    def press_ok_button(self):
        self.okButton.click()

    def press_send_button_on_almost_there_screen(self):
        self.sendButtonOnAlmostThereScreen.click()

    def press_link_acc_breadcrumb(self):
        self.linkAccBreadCrumb.click()

# ---------------Asserts-------------------------------

    def check_if_documents_page_is_loaded(self):
       assert self.is_element_present("reviewDocumentsHeader", timeout=20), "Unable to load Review Documents Page"

    def check_if_almost_there_shown(self):
       assert self.is_element_present("almostThereHeader", timeout=20), "Almost there! screen was not shown"

    def check_if_congrats_massage_was_shown(self):
       assert self.is_element_present("congrats", timeout=20), "Congratulations! message was not shown"
