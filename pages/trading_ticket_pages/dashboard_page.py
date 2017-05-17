from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage


class DashboardPage(AbstractBasePage):
    tradingHeader = Find(by=By.XPATH, value='.//*[text()="Trading"]')
    manageTrading = Find(by=By.XPATH, value='.//*[text()="Trading"]/following-sibling::*[text()="Manage"]')
    managePerformance = Find(by=By.XPATH, value='.//*[text()="Performance"]/following-sibling::*[text()="Manage"]')
    manageResearch = Find(by=By.XPATH, value='.//*[text()="Research"]/following-sibling::*[text()="Manage"]')

    def __init__(self):
            AbstractBasePage.__init__(self, "http://operations.stratifi.com/")

    # ------------Clicks------------------------------

    def press_manage_trading(self):
        self.manageTrading.click()

    # ------------Send Keys------------------------------

    # ---------------Asserts-------------------------------

    def check_if_trading_ticket_page_is_loaded(self):
       assert self.is_element_present("tradingHeader", timeout=10), "Trading ticket page was not loaded"



