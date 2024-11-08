from selenium.webdriver.common.by import By

from base.wait import wait


class verveDashboardPage(wait):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
        self.wait_for_page_to_load()

    circular_count = (By.ID, "lblCircularCount")
    external_circular_count = (By.ID, "lblExternalCircular")
    internal_circular_count = (By.ID, "lblInternalCircular")
    add_announcement_button = (By.XPATH, "//div[@id='divAddAnnouncement']/a")

    @property
    def getAddAnnouncementButton(self):
        return self.wait_for_element(By.XPATH, "//div[@id='divAddAnnouncement']/a")

    def getCircularCount(self):
        circular_count = self.driver.find_element(*verveDashboardPage.circular_count)
        return circular_count

    def getExternalCircularCount(self):
        external_circular_count = self.driver.find_element(*verveDashboardPage.external_circular_count)
        return external_circular_count

    def getInternalCircularCOunt(self):
        internal_circular_count = self.driver.find_element(*verveDashboardPage.internal_circular_count)
        return internal_circular_count
