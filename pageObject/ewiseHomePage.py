from selenium.webdriver.common.by import By


class ewiseHomePage:
    def __init__(self, driver):
        self.driver = driver

    tiles = (By.XPATH, "//div[@id='da-thumbs']/div/div/ul/li/a")
    verve_tile = (By.XPATH, "//div[@id='dvMaxLife']/ul/li/a")

    def getTiles(self):
        tiles = self.driver.find_elements(*ewiseHomePage.tiles)
        return tiles

    def getverveTile(self):
        verve_tile = self.driver.find_element(*ewiseHomePage.verve_tile)
        return verve_tile
