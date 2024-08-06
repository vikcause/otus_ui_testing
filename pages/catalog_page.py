"""Module for working with OpenCart header elements on page"""

from pages.main_page import WORKWITHPAGE


class CatalogPage(WORKWITHPAGE):
    """basic class to work with elements on Smartphones page"""

    PATH = "/en-gb/catalog/smartphone"

    def page_open(self, default_url):
        """method for open browser"""

        self.browser.get(default_url + self.PATH)
