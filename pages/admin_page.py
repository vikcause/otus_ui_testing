"""Module for testing OpenCart admin page"""


from selenium.webdriver.common.by import By
from pages.work_with_page import WORKWITHPAGE


class AdminPage(WORKWITHPAGE):
    """basic class to work with elements on Admin page"""

    path = "/administration"
    username_work = By.CSS_SELECTOR, "#input-username"
    password_work = By.CSS_SELECTOR, "#input-password"
    login_button_submit = By.CSS_SELECTOR, ".btn.btn-primary"
    catalog_menu = By.XPATH, "//*[text()=' Catalog']"
    products_menu = By.XPATH, "//*[text()='Products']"
    add_new_product = By.XPATH, '//*[@id="content"]/div[1]/div/div/a'
    product_name_field = By.CSS_SELECTOR, "#input-name-1"
    meta_tag_field = By.CSS_SELECTOR, "#input-meta-title-1"
    data_tab = By.XPATH, "//*[text()='Data']"
    seo_tab = By.XPATH, "//*[text()='SEO']"
    input_model = By.CSS_SELECTOR, "#input-model"
    input_price = By.CSS_SELECTOR, "#input-price"
    input_quantity = By.CSS_SELECTOR, "#input-quantity"
    seo_name_input = By.CSS_SELECTOR, "#input-keyword-0-1"
    save_product_button = By.CSS_SELECTOR, ".fa-solid.fa-floppy-disk"
    last_page = By.XPATH, "//*[text()='>|']"
    last_product = (By.XPATH,
                    "//div[1]/table/tbody/tr[9]/td[1]/input")
    popup_success = (By.XPATH,
                     "//div[contains(text(),'Success: "
                     "You have modified products!')]")
#   text()='position()<last()' ask how to use position last
    def page_open(self, default_url):
        """method for open browser"""

        self.browser.get(default_url + self.path)

    def input_username(self, text):
        """method for input username with clear field"""

        self.find_element(self.username_work).clear()
        self.find_element(self.username_work).send_keys(text)

    def input_password(self, text):
        """method for input password with clear field"""

        self.find_element(self.password_work).clear()
        self.find_element(self.password_work).send_keys(text)

    def login(self, username, password):
        """method for login to admin page"""

        self.find_element(self.username_work).clear()
        self.find_element(self.password_work).clear()
        self.input_text(self.username_work, username)
        self.input_text(self.password_work, password)
        self.find_element(self.login_button_submit).click()

    def submit_login(self):
        """method for press tu submit button"""

        self.find_element(self.login_button_submit).click()

    def title_username(self):
        """method for find username title name"""

        self.find_element((By.CSS_SELECTOR, ".rounded-circle"))
        profile = self.find_element((By.CSS_SELECTOR, ".rounded-circle"))
        return profile.get_attribute("title")

    def alt_username(self):
        """method for find username alt name"""

        self.find_element((By.CSS_SELECTOR, ".rounded-circle"))
        profile = self.find_element((By.CSS_SELECTOR, ".rounded-circle"))
        return profile.get_attribute("alt")

    def select_catalog(self):
        """method for open catalog menu"""

        self.find_element(self.catalog_menu).click()

    def select_products(self):
        """method for opening catalog products list"""

        self.find_element(self.products_menu).click()

    def add_product(self):
        """method for click to add new product button"""

        self.find_element(self.add_new_product).click()

    def add_product_name(self, text):
        """method for enter product name"""

        self.input_text(self.product_name_field, text)

    def add_meta_tag(self, text):
        """method for enter product meta tag"""

        self.input_text(self.meta_tag_field, text)

    def select_data_tab(self):
        """method for select Data tab"""

        self.find_element(self.data_tab).click()

    def add_model(self, text):
        """method for enter model name"""

        self.input_text(self.input_model, text)

    def add_price(self, text):
        """method for enter model price"""

#        self.input_text(self.input_price, text)
        self.find_element(self.input_price).clear()
        self.find_element(self.input_price).send_keys(text)

    def add_quantity(self, text):
        """method for enter model name"""

#        self.input_text(self.input_quantity, text)
        self.find_element(self.input_quantity).clear()
        self.find_element(self.input_quantity).send_keys(text)

    def select_seo_tab(self):
        """method for select Seo tab"""

        self.find_element(self.seo_tab).click()

    def add_seo_name(self, text):
        """method for enter SEO mark name"""

        self.input_text(self.seo_name_input, text)

    def save_product(self):
        """method for press SAVE button"""

        self.find_element(self.save_product_button).click()

    def go_to_the_last_page(self):
        """method for go to the last product page"""

        self.find_element((self.last_page)).click()

    def select_last_product(self):
        """method for select last product"""

        self.find_element((self.last_product)).click()

    def delete_product(self):
        """method for delete product"""

        self.find_element((By.CSS_SELECTOR, ".btn.btn-danger")).click()
        confirm_alert = self.browser.switch_to.alert
        confirm_alert.accept()

    def find_popup_success(self):
        """method for find success pop-up"""

        self.find_element(self.popup_success)

    def scroll_down(self):
        """method for scroll page to bottom"""

        self.browser.execute_script(
           "window.scrollTo(0, 600);")

    def scroll_up(self):
        """method for scroll page up"""

        self.browser.execute_script(
            "window.scrollTo(2000, 0);")
