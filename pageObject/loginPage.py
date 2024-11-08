from selenium.webdriver.common.by import By


class loginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "inpUserName")
    password = (By.NAME, "inpPassword")
    login_button = (By.ID, "btnEwiseLogin")

    def getUsername(self):
        username = self.driver.find_element(*loginPage.username)
        return username

    def getPassword(self):
        password = self.driver.find_element(*loginPage.password)
        return password

    def getLoginButton(self):
        login_button = self.driver.find_element(*loginPage.login_button)
        return login_button
