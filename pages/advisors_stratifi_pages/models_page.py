from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage
import unittest


class ModelsPage(AbstractBasePage, unittest.TestCase):
    createdModelsHeader = Find(by=By.XPATH, value='.//*[text()="Created Models"]')
    targetModel = Find(by=By.XPATH, value='.//*[text()="Model for autotest"]')
    archiveButtonForTargetModel = Find(by=By.XPATH, value='.//*[text()="Model for autotest"]/following::*[text()="Archive"]')

    def __init__(self):
            AbstractBasePage.__init__(self, "https://advisors.stratifi.com/advisor/models")

# --------------Clicks-----------------------

    def press_archive_button_for_target_model(self):
        self.archiveButtonForTargetModel.click()

# ---------------Asserts-------------------------------

    def check_models_page_loaded(self):
       assert self.is_element_present("createdModelsHeader", timeout=10), "Models page was not loaded"

    def check_if_created_model_is_in_the_list(self):
       assert self.is_element_present("targetModel", timeout=10), "Unable to find a target model"

    def check_if_target_model_was_deleted(self):
        self.assertFalse(self.is_element_present("targetModel", timeout=10), "Target model was not deleted")
