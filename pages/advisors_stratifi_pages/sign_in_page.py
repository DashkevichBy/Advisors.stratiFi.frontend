from selenium.webdriver.common.by import By
from webium import Find
from abstract_base_page import AbstractBasePage


class SignInPage(AbstractBasePage):
    emailField = Find(by=By.XPATH, value='.//*[@name="email"]')
    passwordField = Find(by=By.XPATH, value='.//*[@name="password"]')
    signInButton = Find(by=By.XPATH, value='.//*[text()="Sign in"]')

    def __init__(self):
            AbstractBasePage.__init__(self, "https://advisors.stratifi.com/")

    # ------------Clicks------------------------------

    def press_sign_in(self):
        self.signInButton.click()

    # ------------Send Keys------------------------------

    def enter_login(self, login):
        self.emailField.send_keys(login)

    def enter_password(self, password):
        self.passwordField.send_keys(password)




