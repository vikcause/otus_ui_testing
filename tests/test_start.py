"""Module for testing OpenCart WebPages"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.header import Header
from pages.catalog_page import CatalogPage
from pages.admin_page import AdminPage
from pages.registration_page import RegistrationPage


def test_main_page(browser, default_url):
    """Function for testing OpenCart main Page"""

    browser.get(default_url)
    wait = WebDriverWait(browser, 5, [1])

    wait.until(EC.title_is("Your Store"))
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "div.col-md-3.col-lg-4")))
    wait.until(EC.visibility_of_element_located((
        By.XPATH, "//*[@id='header-cart']"))).click()
    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "#header-cart > div > ul > li"),
        "Your shopping cart is empty!"))
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#carousel-banner-0")))
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "div#logo")))
    wait.until(EC.element_to_be_clickable((
        By.XPATH, "/html/body/main/div[2]/div/div/div[3]/div[1]/button[3]")))
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#narbar-menu > ul > li:nth-child(7) > a"),
        "Cameras"))


def test_catalog_page(browser, default_url):
    """Function for testing OpenCart smartphones catalog page"""

    browser.get(f"{default_url}/en-gb/catalog/smartphone")
    wait = WebDriverWait(browser, 7, [1])

    wait.until(EC.url_contains("/catalog/smartphone"))
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#compare-total")))
    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "#content > h2"), "Phones & PDAs"))
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#button-list"))).click()
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "//*[@id='product-list']/div[3]/div/div[2]/div/h4/a")))


def test_item_page(browser, default_url):
    """Function for testing OpenCart iphone item page"""

    browser.get(f"{default_url}/en-gb/product/smartphone/iphone")
    wait = WebDriverWait(browser, 5, [1])

    wait.until(EC.text_to_be_present_in_element_value((
        By.CSS_SELECTOR, "#input-quantity"), "1"))
    wait.until(EC.title_is("iPhone"))
    wait.until(
        EC.text_to_be_present_in_element((
            By.CSS_SELECTOR,
            "#content > div.row.mb-3 > div:nth-child(2) > ul:nth-child(3) >"
            " li:nth-child(1) > h2 > span"), "$123.20"))
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#content > div.row.mb-3 > div:nth-child(1) > div > "
                         "a > img"))).click()
    wait.until(EC.element_to_be_clickable((
        By.XPATH, "/html/body/div[2]/div/button[2]"))).click()


def test_admin_page(browser, default_url):
    """Function for testing OpenCart administration page"""

    browser.get(f"{default_url}/administration")
    wait = WebDriverWait(browser, 4, [1])

    wait.until(EC.title_is("Administration"))
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#content > div > div > div > div > div.card-body")))
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".fa-solid.fa-lock")))
    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "#form-login > div:nth-child(1) > label"),
        "Username"))
    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "#form-login > div:nth-child(2) > label"),
        "Password"))
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#form-login > div.text-end > button")))


def test_registration_page(browser, default_url):
    """Function for testing OpenCart register Page"""

    browser.get(f"{default_url}/index.php?route=account/register")
    wait = WebDriverWait(browser, 3, [1])

    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#form-register > div > div > input")))
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, "#input-newsletter")))
    wait.until(EC.text_to_be_present_in_element((
        By.CSS_SELECTOR, "#content > h1"), "Register Account"))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#account")))
    wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, "#form-register > fieldset:nth-child(2)")))


def test_login_adm_page(browser, default_url):
    """Function for testing login to OpenCart administration page"""

    browser.get(f"{default_url}/administration")
    wait = WebDriverWait(browser, 5, [1])
    adm_login_page_title = EC.title_is("Administration")
    adm_user_page_title = EC.title_is("Dashboard")

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#input-username"))).clear()
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#input-username"))).send_keys("user")
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#input-password"))).clear()
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#input-password"))).send_keys("bitnami")
    wait.until(EC.element_to_be_clickable((
        By.CSS_SELECTOR, ".btn.btn-primary"))).click()
    WebDriverWait(browser, 5).until(adm_user_page_title)
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".rounded-circle")))
    wait.until(EC.text_to_be_present_in_element_attribute(
        (By.CSS_SELECTOR, ".rounded-circle"),
        "alt", "John Doe"))
    wait.until(EC.text_to_be_present_in_element_attribute(
        (By.CSS_SELECTOR, ".rounded-circle"),
        "title", "user"))
    wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".card-header"), "World Map"))
    wait.until(EC.element_to_be_clickable((
        By.XPATH,
        "/ html / body / div[1] / header / div / ul / li[4] / a / i"))).click()
    WebDriverWait(browser, 5).until(adm_login_page_title)


def test_add_to_cart(browser, default_url):
    """Function for testing add item to cart OpenCart main page"""

    main_page = MainPage(browser)
    main_page.page_open(default_url)
    main_page.scroll_down()
    main_page.add_product_to_cart()
    product_name_listing = main_page.get_product_name_listing()
    main_page.scroll_up()
    main_page.click_cart_button()
    product_name_cart = main_page.get_product_name_cart()
    assert product_name_listing == product_name_cart


def test_change_currency_from_main_page(browser, default_url):
    """Function for testing changing currency on main page"""

    main_page = MainPage(browser)
    header = Header(browser)
    main_page.page_open(default_url)
    header.click_currency()
    header.select_euro()
    header.click_currency()
    header.select_pound()
    price = main_page.get_price_value()
    assert price.__contains__("£")
    assert not price.__contains__("€")
    assert not price.__contains__("$")


def test_change_currency_from_catalog_page(browser, default_url):
    """Function for testing changing currency on main page"""

    catalog_page = CatalogPage(browser)
    header = Header(browser)
    catalog_page.page_open(default_url)
    header.click_currency()
    header.select_pound()
    header.click_currency()
    header.select_euro()
    price = MainPage(browser).get_price_value()
    assert price.__contains__("€")
    assert not price.__contains__("$")
    assert not price.__contains__("£")


def test_add_product(browser, default_url):
    """method for add new product"""

    admin_page = AdminPage(browser)
    admin_page.page_open(default_url)
    admin_page.login("user", "bitnami")
    admin_page.select_catalog()
    admin_page.select_products()
    admin_page.add_product()
    admin_page.add_product_name("test product")
    admin_page.add_meta_tag("test123")
    admin_page.select_data_tab()
    admin_page.add_model("321test")
    admin_page.scroll_down()
    admin_page.add_price("999.0")
    admin_page.add_quantity("15")
    admin_page.scroll_up()
    admin_page.select_seo_tab()
    admin_page.add_seo_name("product_test")
    admin_page.save_product()
    admin_page.find_popup_success()


def test_delete_product(browser, default_url):
    """method for delete product"""

    admin_page = AdminPage(browser)
    admin_page.page_open(default_url)
    admin_page.login("user", "bitnami")
    admin_page.select_catalog()
    admin_page.select_products()
    admin_page.scroll_down()
    admin_page.go_to_the_last_page()
    admin_page.select_last_product()
    admin_page.scroll_up()
    admin_page.delete_product()
    admin_page.find_popup_success()


def test_user_registration(browser, default_url):
    """method for user registration"""

    registration_page = RegistrationPage(browser)
    registration_page.page_open(default_url)
    registration_page.input_data(
        "Test", "User", "test@test.net", "12345678")
    registration_page.subscribe_news()
    registration_page.confirm_agreement()
    registration_page.complete_registration()
    title_text = registration_page.get_title_text()
    assert title_text == "Your Account Has Been Created!"
    registration_page.complete_registration()
    WebDriverWait(browser, 5).until(EC.title_is("My Account"))


def test_change_currency(browser, default_url):
    """method for change currencies from pages"""

    header = Header(browser)
    CatalogPage(browser).page_open(default_url)
    header.click_currency()
    header.select_pound()
    currency_icon = header.get_currency_icon()
    assert currency_icon == "£"
    header.click_currency()
    header.select_euro()
    currency_icon = header.get_currency_icon()
    assert currency_icon == "€"
    header.click_currency()
    header.select_dollar()
    currency_icon = header.get_currency_icon()
    assert currency_icon == "$"
