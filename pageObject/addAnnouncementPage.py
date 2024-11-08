from selenium.webdriver.common.by import By

from base.wait import wait


class addAnnouncementPage(wait):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)
        self.wait_for_page_to_load()

    add_announcement_frame = (By.XPATH, "//iframe[@class='cboxIframe']")
    title_text_box = (By.ID, "txtTitle")
    announcement_type_dropdown = (By.ID, "ddlAnnouncementType")
    circular_no_text_box = (By.ID, "txtCircularNo")
    circular_issue_date_text_box = (By.ID, "txtCircularIssueDate")
    dates = (By.XPATH, "//div[@class='datepicker-days']/table/tbody/tr/td")
    circular_sub_type_dropdown = (By.ID, "ddlCircularType")
    sub_type_dropdown = (By.ID, "ddlSubType")
    description_text_box = (By.ID, "txtDescription")
    shared_dropdown = (By.ID, "MainContent_ddlShared")
    department_checkboxes = (By.XPATH, "//table[@id='MainContent_gvDepartment']/tbody/tr/td[2]")
    location_checkboxes = (By.XPATH, "//table[@id='MainContent_gvLocation']/tbody/tr/td[2]")
    date_restriction_dropdown = (By.ID, "MainContent_ddlDateRestriction")
    expiry_date_text_box = (By.ID, "txtExpirtDate")
    expiry_date_datepicker_month_and_year_header = (By.XPATH, "//div[@class='datepicker-days']/table/thead/tr/th[2]")
    datepicker_year_header = (By.XPATH, "//div[@class='datepicker-months']/table/thead/tr/th[2]")
    datepicker_next_button = (By.XPATH, "//div[@class='datepicker-months']/table/thead/tr/th[3]")
    expiry_date_datepicker_months = (By.XPATH, "//div[@class='datepicker-months']/table/tbody/tr/td/span")
    expiry_date_datepicker_days = (By.XPATH, "//div[@class='datepicker-days']/table/tbody/tr/td")
    attach_file_dropdown = (By.ID, "MainContent_ddlAttachFile")
    choose_file_button = (By.ID, "File_Attchment")
    upload_file_button = (By.ID, "btnFileUpload")
    save_button = (By.ID, "btnAdd")

    def getAnnouncementTypeDropdown(self):
        announcement_type_dropdown = self.driver.find_element(*addAnnouncementPage.announcement_type_dropdown)
        return announcement_type_dropdown

    def getTitleTextBox(self):
        title_text_box = self.driver.find_element(*addAnnouncementPage.title_text_box)
        return title_text_box

    def getCircularNoTextBox(self):
        circular_no_text_box = self.driver.find_element(*addAnnouncementPage.circular_no_text_box)
        return circular_no_text_box

    def getCicrularIssueDate(self):
        circular_issue_date_text_box = self.driver.find_element(*addAnnouncementPage.circular_issue_date_text_box)
        return circular_issue_date_text_box

    def getDates(self):
        dates = self.driver.find_elements(*addAnnouncementPage.dates)
        return dates

    def getCircularSubTypeDropdown(self):
        circular_sub_type_dropdown = self.driver.find_element(*addAnnouncementPage.circular_sub_type_dropdown)
        return circular_sub_type_dropdown

    def getSubTypeDropdown(self):
        sub_type_dropdown = self.driver.find_element(*addAnnouncementPage.sub_type_dropdown)
        return sub_type_dropdown

    def getDescriptionTextBox(self):
        description_text_box = self.driver.find_element(*addAnnouncementPage.description_text_box)
        return description_text_box

    def getSharedDropdown(self):
        shared_dropdown = self.driver.find_element(*addAnnouncementPage.shared_dropdown)
        return shared_dropdown

    def getDepartmentCheckboxes(self):
        department_checkboxes = self.driver.find_elements(*addAnnouncementPage.department_checkboxes)
        return department_checkboxes

    def getLocationCheckboxes(self):
        location_checkboxes = self.driver.find_elements(*addAnnouncementPage.location_checkboxes)
        return location_checkboxes

    def getDateRestrictionDropdown(self):
        date_restriction_dropdown = self.driver.find_element(*addAnnouncementPage.date_restriction_dropdown)
        return date_restriction_dropdown

    def getExpiryDateTextBox(self):
        expiry_date_text_box = self.driver.find_element(*addAnnouncementPage.expiry_date_text_box)
        return expiry_date_text_box

    def getExpiryDateDatepickerMonthAndYearHeader(self):
        expiry_date_datepicker_month_and_year_header = self.driver.find_element(
            *addAnnouncementPage.expiry_date_datepicker_month_and_year_header)
        return expiry_date_datepicker_month_and_year_header

    def getExpiryDateDatepickerYearHeader(self):
        datepicker_year_header = self.driver.find_element(*addAnnouncementPage.datepicker_year_header)
        return datepicker_year_header

    def getDatePickerNextButton(self):
        datepicker_next_button = self.driver.find_element(*addAnnouncementPage.datepicker_next_button)
        return datepicker_next_button

    def getExpiryDateDatepickerMOnths(self):
        expiry_date_datepicker_months = self.driver.find_elements(*addAnnouncementPage.expiry_date_datepicker_months)
        return expiry_date_datepicker_months

    def getExpiryDateDatepickerDays(self):
        expiry_date_datepicker_days = self.driver.find_elements(*addAnnouncementPage.expiry_date_datepicker_days)
        return expiry_date_datepicker_days

    def getAttachFileDropdown(self):
        attach_file_dropdown = self.driver.find_element(*addAnnouncementPage.attach_file_dropdown)
        return attach_file_dropdown

    def getChooseFileButton(self):
        choose_file_button = self.driver.find_element(*addAnnouncementPage.choose_file_button)
        return choose_file_button

    def getUploadFileButton(self):
        upload_file_button = self.driver.find_element(*addAnnouncementPage.upload_file_button)
        return upload_file_button

    def getSaveButton(self):
        save_button = self.driver.find_element(*addAnnouncementPage.save_button)
        return save_button

    @property
    def getAddAnnouncementFrame(self):
        return self.wait_for_element(By.XPATH, "//iframe[@class='cboxIframe']")
