"""Base module for working with OpenCart pages"""


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class WORKWITHPAGE:
    """basic class to work with elements on pages"""

    def __init__(self, browser, wait=5):
        """init method"""

        self.wait = WebDriverWait(browser, wait)
        self.browser = browser
        self.actions = ActionChains(browser)

    def page_open(self, default_url):
        """method for open pages"""

        self.browser.get(default_url)

    def find_element(self, locator: tuple, timeout=5):
        """method to find one element"""

        return (WebDriverWait(self.browser, timeout).
                until(EC.element_to_be_clickable((locator))))

    def find_elements(self, locator: tuple, timeout=5):
        """method to find all needed elements"""

        return (WebDriverWait(self.browser, timeout).
                until(EC.visibility_of_all_elements_located(locator)))

    def click_to_elements(self, locator: tuple):
        """method to click to several elemetns with pause"""

        ActionChains(self.browser).move_to_element(
            self.find_elements(locator)).pause(1).click().perform()

    def input_text(self, locator: tuple, text: str):
        """method to input text letter by letter"""

        self.find_element(locator).click()
        self.find_element(locator).clear()
        for i in text:
            self.find_element(locator).send_keys(i)
