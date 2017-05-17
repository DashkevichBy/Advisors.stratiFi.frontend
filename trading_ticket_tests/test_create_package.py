import logging
import os

import pytest

from common import BaseTest
from pages.trading_ticket_pages.dashboard_page import DashboardPage
from pages.trading_ticket_pages.packages_page import PackagesPage
from pages.trading_ticket_pages.packages_create_page import PackagesCreatePage

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


class TestCreatePackage(BaseTest):
    dashboard_page = DashboardPage()
    packages_page = PackagesPage()
    packages_create_page = PackagesCreatePage()
    dashboard_page.open()

    def test_create_package(self):
        self.dashboard_page.check_if_trading_ticket_page_is_loaded()
        print('Dashboard page was opened: ' + str(self.dashboard_page.is_element_present('tradingHeader', timeout=10)))
        self.dashboard_page.press_manage_trading()
        self.packages_page.check_if_trading_ticket_page_is_loaded()
        print('Packages page was opened: ' + str(self.packages_page.is_element_present('packagesHeader', timeout=10)))
        self.packages_page.press_create_a_package()
        self.packages_create_page.check_if_create_a_package_page_is_loaded()
        self.packages_create_page.enter_package_name("Autotest package")
        self.packages_create_page.select_the_first_strategy()
        self.packages_create_page.check_if_there_is_at_least_one_account()




if __name__ == "__main__":
    mylogger.info(' About to start ')
    pytest.main(args=['-s', os.path.abspath(__file__)])
    mylogger.info(' Done executing ')
