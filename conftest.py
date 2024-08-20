"""
fixtures and addoptions to work with opencart
"""
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.service import Service as FFService
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    """addoptions for running with cmd"""

    parser.addoption(
        "--browser", default="ch", choices=["ya", "ch", "ff"],
        help="choose browser"
    )
    parser.addoption(
        "--headless", action="store_true", help="headless option"
    )
    parser.addoption(
        "--yadriver", action="store_true", help="ya driver path",
        default="./yandex_driver/yandexdriver"
    )
    parser.addoption(
        "--default_url", default="http://192.168.1.243:8081/"
    )


@pytest.fixture()
def default_url(request):
    """fixture for open base url opencart"""

    return request.config.getoption("--default_url")


# better made not higher than scope="function"
@pytest.fixture()
def browser(request):
    """fixture for running different browsers from cmd"""

    browser_name = request.config.getoption("--browser")
    headless_mode = request.config.getoption("--headless")
    yadriver = request.config.getoption("--yadriver")

    if browser_name == "ya":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        options.binary_location = "/usr/bin/yandex-browser"
        service = Service(executable_path=yadriver)
        browser = webdriver.Chrome(service=service, options=options)
    elif browser_name == "ch":
        options = Options()
        if headless_mode:
            options.add_argument("headless=new")
        browser = webdriver.Chrome(service=Service(), options=options)
    elif browser_name == "ff":
        options = FFOptions()
        if headless_mode:
            options.add_argument("--headless")
        browser = webdriver.Firefox(service=FFService())
    else:
        raise ValueError(f"Browser {browser_name} isn't supported")

#    browser.maximize_window() or
#    browser.set_window_size() able to use instead
#    browser.set_window_size(1920, 1080)
    browser.maximize_window()

    yield browser

    browser.close()
