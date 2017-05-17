from webium import BasePage
from stratifi_tests.common import Driver


class AbstractBasePage(BasePage):

    def __init__(self, url):
        BasePage.__init__(self, Driver.get(), url)

    def get_title(self):
        return Driver.get().title

    def close_tabs(self):
        return Driver.get("")