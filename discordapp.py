from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time


default_url = 'https://discordapp.com/channels/@me'
delay = 1
login_url = 'https://discordapp.com/login'
timeout = 15


class Discordapp:
    def __init__(self):
        # Create instance of Chrome driver in incognito mode
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(options=options)

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
            wait = WebDriverWait(self.driver, timeout)
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
        wait = WebDriverWait(self.driver, timeout)

        # Wait for login form to load
        try:
            wait.until(EC.presence_of_element_located((By.TAG_NAME, 'input')))
        except:
            return False

        # Find login input elements
        inputs = self.driver.find_elements_by_tag_name('input')

        # Input email
        inputs[0].clear()
        inputs[0].send_keys(email)

        # Input password and return
        inputs[1].clear()
        inputs[1].send_keys(password, Keys.RETURN)

        # Wait for redirect to default URL
        try:
            wait.until(EC.url_to_be(default_url))
            return True
        except:
            return False

    def send(self, message: str) -> None:
        # Send message
        message_box = self.driver.find_element_by_class_name('textArea-2Spzkt')
        message_box.clear()
        message_box.send_keys(message, Keys.RETURN)

        # Delay for processing
        time.sleep(delay)
