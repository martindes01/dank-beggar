from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time


# Message box css selector correct as of version 'Stable 57334 (b1437cc)' released 10/03/2020
default_css_selector = '.slateTextArea-1Mkdgw'

default_delay = 0.5
default_timeout = 10
login_url = 'https://discordapp.com/login'


class Discordapp:
    def __init__(self):
        # Create instance of Chrome driver without GUI
        options = webdriver.ChromeOptions()
        options.headless = True
        options.add_argument('--incognito')
        options.add_argument('--disable-logging')
        self.driver = webdriver.Chrome(options=options)

        # Define timing attributes and set to default values
        self.css_selector = default_css_selector
        self.delay = default_delay
        self.timeout = default_timeout

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Close Chrome driver
        self.driver.quit()

    def load(self, url: str) -> bool:
        # Navigate to server channel
        self.driver.get(url)

        # Wait for redirect away from server channel
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            wait.until_not(EC.url_to_be(url))

            # Redirect; return False
            return False
        except:
            # No redirect; return True
            return True

    def login(self, email: str, password: str) -> bool:
        # Navigate to login page
        self.driver.get(login_url)

        # Create WebDriverWait object
        wait = WebDriverWait(self.driver, self.timeout)

        # Wait for login form to load
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
        except:
            return False

        # Find login input elements
        inputs = self.driver.find_elements_by_tag_name('input')

        # Input email address and password then return
        inputs[0].send_keys(email)
        inputs[1].send_keys(password, Keys.RETURN)

        # Wait for redirect away from login URL
        try:
            wait.until_not(EC.url_to_be(login_url))
            return True
        except:
            return False

    def send(self, message: str) -> None:
        try:
            # Send message
            self.driver.find_element_by_css_selector(self.css_selector).send_keys(message, Keys.RETURN)

            # Delay for processing
            time.sleep(self.delay)
        except:
            pass
