from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from base.base import base
from pageObject.addAnnouncementPage import addAnnouncementPage
from pageObject.ewiseHomePage import ewiseHomePage
from pageObject.loginPage import loginPage
from pageObject.verveDashboardPage import verveDashboardPage
from testData.addCircularData import *
from testData.baseData import *
from testData.loginData import *


class Testlogin(base):

    @pytest.mark.skip
    def test_to_verify_login_and_navigate_to_verve_tile(self, getSuperAdminLoginData):
        a = ActionChains(self.driver)
        a.click().perform()
        login_page_object = loginPage(self.driver)
        username = login_page_object.getUsername()
        password = login_page_object.getPassword()
        login_button = login_page_object.getLoginButton()
        super().enterData(username, getSuperAdminLoginData["username"])
        super().enterData(password, getSuperAdminLoginData["password"])
        super().buttonClick(login_button)
        ewise_home_page_obejct = ewiseHomePage(self.driver)
        getVerveTile = ewise_home_page_obejct.getverveTile()
        super().buttonClick(getVerveTile)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    @pytest.mark.skip
    def test_to_verify_count_of_circular(self, getSuperAdminLoginData):
        self.test_to_verify_login_and_navigate_to_verve_tile(getSuperAdminLoginData)
        verve_dashboard_page_object = verveDashboardPage(self.driver)
        circular_count = verve_dashboard_page_object.getCircularCount().text
        external_circular_count = verve_dashboard_page_object.getExternalCircularCount().text
        internal_circular_count = verve_dashboard_page_object.getInternalCircularCOunt().text

        assert int(circular_count) == int(external_circular_count) + int(internal_circular_count)

    @pytest.mark.skip
    def test_to_add_internal_circular_tc3(self, getSuperAdminLoginData):
        self.test_to_verify_login_and_navigate_to_verve_tile(getSuperAdminLoginData)
        verve_dashboard_page_object = verveDashboardPage(self.driver)

        super().buttonClick(verve_dashboard_page_object.getAddAnnouncementButton)
        add_announcement_page_object = addAnnouncementPage(self.driver)

        super().switchToFrame(add_announcement_page_object.getAddAnnouncementFrame)
        add_circular_data = getAddCircularDataTc3()
        add_announcement_page_object = addAnnouncementPage(self.driver)
        add_announcement_page_object.getTitleTextBox().send_keys(add_circular_data["title"])
        super().selectDropdown(add_announcement_page_object.getAnnouncementTypeDropdown(),
                               add_circular_data["announcement_type"])
        super().enterData(add_announcement_page_object.getCircularNoTextBox(), add_circular_data["circular_no"])

        super().ActionChains().move_to_element(add_announcement_page_object.getCicrularIssueDate()).click().perform()

        super().selectDate(add_announcement_page_object.getDates(), add_circular_data["circular_issue_date"])
        super().selectDropdown(add_announcement_page_object.getCircularSubTypeDropdown(),
                               add_circular_data["internal_circular_value"])
        super().selectDropdown(add_announcement_page_object.getSubTypeDropdown(),
                               add_circular_data["internal_sub_type_value"])
        super().enterData(add_announcement_page_object.getDescriptionTextBox(), add_circular_data["description"])
        super().selectDropdown(add_announcement_page_object.getSharedDropdown(), add_circular_data["shared_value"])
        super().selectCheckbox(add_announcement_page_object.getDepartmentCheckboxes(),
                               add_circular_data["department_value"])
        super().selectCheckbox(add_announcement_page_object.getLocationCheckboxes(),
                               add_circular_data["location_value"])
        super().selectDropdown(add_announcement_page_object.getDateRestrictionDropdown(),
                               add_circular_data["date_restriction"])
        super().ActionChains().move_to_element(add_announcement_page_object.getExpiryDateTextBox()).click().perform()

        super().buttonClick(add_announcement_page_object.getExpiryDateDatepickerMonthAndYearHeader())

        super().selectYear(add_announcement_page_object.getExpiryDateDatepickerYearHeader(), add_circular_data[
            "expiry_date_year_header"], add_announcement_page_object.getDatePickerNextButton())

        super().selectMonth(add_announcement_page_object.getExpiryDateDatepickerMOnths(),
                            add_circular_data["expiry_date_month"])
        super().selectDate(add_announcement_page_object.getExpiryDateDatepickerDays(), add_circular_data["expiry_date"])

        super().selectDropdown(add_announcement_page_object.getAttachFileDropdown(),
                               add_circular_data["attach_file_value"])

        project_path = getProjectPath()

        add_announcement_page_object.getChooseFileButton().send_keys(project_path + "\\files\\ddd.txt")
        super().buttonClick(add_announcement_page_object.getUploadFileButton())
        print("xyz")

    def test_to_verify_internal_sub_type_values_tc4(self, getSuperAdminLoginData):
        self.test_to_verify_login_and_navigate_to_verve_tile(getSuperAdminLoginData)
        verve_dashboard_page_object = verveDashboardPage(self.driver)
        super().buttonClick(verve_dashboard_page_object.getAddAnnouncementButton)

        add_announcement_page_object = addAnnouncementPage(self.driver)

        super().switchToFrame(add_announcement_page_object.getAddAnnouncementFrame)
        add_circular_data = getAddCircularDataTc4()
        add_announcement_page_object = addAnnouncementPage(self.driver)
        add_announcement_page_object.getTitleTextBox().send_keys(add_circular_data["title"])
        super().selectDropdown(add_announcement_page_object.getAnnouncementTypeDropdown(),
                               add_circular_data["announcement_type"])
        super().enterData(add_announcement_page_object.getCircularNoTextBox(), add_circular_data["circular_no"])

        super().ActionChains().move_to_element(add_announcement_page_object.getCicrularIssueDate()).click().perform()

        super().selectDate(add_announcement_page_object.getDates(), add_circular_data["circular_issue_date"])
        circular_sub_type_dropdown = add_announcement_page_object.getCircularSubTypeDropdown()
        i=0
        while i<len(circular_sub_type_dropdown):
            pass