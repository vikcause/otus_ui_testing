"""
Module for testing OpenCart register page
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.work_with_page import WORKWITHPAGE


class RegistrationPage(WORKWITHPAGE):
    """basic class to work with elements on Registration page"""

    path = "/en-gb?route=account/register"
    firstname_field = By.CSS_SELECTOR, "#input-firstname"
    lastname_field = By.CSS_SELECTOR, "#input-lastname"
    email_field = By.CSS_SELECTOR, "#input-email"
    password_field = By.CSS_SELECTOR, "#input-password"
    subscribe_switch_button = By.CSS_SELECTOR, "#input-newsletter"
    agree_switch_button = By.XPATH, "//*[@name='agree']"
    continue_button = By.CSS_SELECTOR, ".btn.btn-primary"
    title = By.XPATH, "//h1"

    def page_open(self, default_url):
        """method for open browser"""

        self.browser.get(default_url + self.path)

    def input_data(self, firstname, lastname, email, password):
        """method for open browser"""

        self.input_text(self.firstname_field, firstname)
        self.input_text(self.lastname_field, lastname)
        self.input_text(self.email_field, email)
        self.input_text(self.password_field, password)

    def subscribe_news(self):
        """method for subscribe to newsletter"""

        self.find_element(self.subscribe_switch_button).click()

    def confirm_agreement(self):
        """method for confirm agreement"""

        self.find_element(self.agree_switch_button).click()

    def complete_registration(self):
        """method for press Continue button"""

        self.find_element(self.continue_button).click()

    def get_title_text(self):
        """method for find success URL"""

        WebDriverWait(self.browser, 5).until(
            EC.url_contains(
                "http://192.168.1.243:8081"
                "/en-gb?route=account/success&customer"))
        title = self.find_element(self.title)
        title_text = title.text
        return title_text
