import time

import pytest
from pages.advisors_stratifi_pages.clients_page import ClientsPage
from pages.advisors_stratifi_pages.link_accounts_page import LinkAccountsPage
from pages.advisors_stratifi_pages.stratifi_page import StratifiPage

from common import BaseTest
from common import Driver
from pages.advisors_stratifi_pages.documents_page import DocumentsPage


class TestOnboarding(BaseTest):
    stratifi_page = StratifiPage()
    clients_page = ClientsPage()
    link_accounts_page = LinkAccountsPage()
    documents_page = DocumentsPage()

    def test_link_acc_and_send_documents(self):
        self.stratifi_page.open()
        self.stratifi_page.check_if_page_is_loaded()
        print('Page is loaded: ' + str(self.stratifi_page.is_element_present('startAnalise')))
        self.stratifi_page.press_client_button()
        self.clients_page.check_if_clients_page_is_opened()
        self.clients_page.press_accnotlinked_button_on_first_available_client()
        self.link_accounts_page.check_if_link_accounts_page_is_opened()
        time.sleep(10)
        self.link_accounts_page.press_create_an_account_button()
        time.sleep(5)
        self.link_accounts_page.select_first_custodian_option()
        time.sleep(5)
        self.link_accounts_page.enter_account_name("Autotest account")
        self.link_accounts_page.enter_random_acc_number()
        self.link_accounts_page.press_create_button()
        time.sleep(5)
        self.link_accounts_page.check_if_new_account_was_added()
        self.link_accounts_page.select_first_acc_type()
        self.link_accounts_page.select_first_doc_type()
        self.link_accounts_page.press_next_button()
        self.documents_page.check_if_documents_page_is_loaded()
        self.documents_page.mark_all_documents_as_signed()
        self.documents_page.press_send_button()
        self.documents_page.check_if_almost_there_shown()
        self.documents_page.press_send_button_on_almost_there_screen()
        self.documents_page.check_if_congrats_massage_was_shown()
        self.documents_page.press_ok_button()
        time.sleep(2)
        self.documents_page.press_link_acc_breadcrumb()
        self.link_accounts_page.check_if_link_accounts_page_is_opened()
        time.sleep(10)
        self.link_accounts_page.press_unlink_acc_button()
        time.sleep(10)
        self.link_accounts_page.check_if_target_account_was_deleted()
        Driver.get().close()




if __name__ == "__main__":
    pytest.main()
