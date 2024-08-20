"""Module for working with OpenCart header elements on page"""

from selenium.webdriver.common.by import By
from pages.work_with_page import WORKWITHPAGE


class Header(WORKWITHPAGE):
    """basic class to work with header elements on pages"""

    CURRENCY_BUTTON = By.XPATH, "//*[text()='Currency']"
    CURRENCY_ICON = By.XPATH, "//strong"

    def page_open(self, default_url):
        """method for open browser"""

        self.browser.get(default_url)

    def click_currency(self):
        """method for open currencies list"""

        self.find_element(self.CURRENCY_BUTTON).click()

    def select_euro(self):
        """method for select euro for currency"""

        self.find_element((By.XPATH, "//*[text()='€ Euro']")).click()

    def select_pound(self):
        """method for select pound for currency"""

        self.find_element((By.XPATH,
                           "//*[text()='£ Pound Sterling']")).click()

    def select_dollar(self):
        """method for select dollar for currency"""

        self.find_element((By.XPATH, "//*[text()='$ US Dollar']")).click()

    def get_currency_icon(self):
        """method for get currency icon statement"""

        icon = self.find_element(self.CURRENCY_ICON)
        icon_text = icon.text
        return icon_text
