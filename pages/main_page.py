"""Module for working with OpenCart home page"""


from selenium.webdriver.common.by import By
from pages.work_with_page import WORKWITHPAGE


class MainPage(WORKWITHPAGE):
    """basic class to work with elements on pages"""

    LISTING_CART_BUTTON = By.CSS_SELECTOR, ".fa-solid.fa-shopping-cart"
    HOMEPAGE_CART_BUTTON = (
        By.CSS_SELECTOR, ".btn.btn-lg.btn-inverse.btn-block.dropdown-toggle")
    PRICE = By.CSS_SELECTOR, ".price-new"

    def page_open(self, default_url):
        """method for open browser"""

        self.browser.get(default_url)

    def scroll_down(self):
        """method for scroll page to bottom"""

        self.browser.execute_script(
           "window.scrollTo(0, 1600);")

    def scroll_up(self):
        """method for scroll page up"""

        self.browser.execute_script("window.scrollTo(1600, 0);")

    def add_product_to_cart(self):
        """method to add item to cart"""

        self.find_element(self.LISTING_CART_BUTTON).click()

    def get_product_name_listing(self):
        """method to get item name"""

        name_product_listing = self.find_element((By.CSS_SELECTOR,
                                                 ".description a"))
        product_listing_text = name_product_listing.get_attribute('text')
        return product_listing_text

    def get_product_name_cart(self):
        """method to get item name from cart"""

        name_product_cart = self.find_element((By.CSS_SELECTOR,
                                              ".text-start a"))
        product_cart_text = name_product_cart.get_attribute('text')
        return product_cart_text

    def click_cart_button(self):
        """method to check on cart button"""

        self.find_element(self.HOMEPAGE_CART_BUTTON).click()

    def get_price_value(self):
        """method to get item currency name"""

        price = self.find_element(self.PRICE).text
        return price
