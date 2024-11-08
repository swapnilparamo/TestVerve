from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class wait:
    def __init__(self, driver, timeout=40):
        self.driver = driver
        self.timeout = timeout

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, self.timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )

    def wait_for_element(self, by, value):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.presence_of_element_located((by, value))
        )