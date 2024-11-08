import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("browser")
class base:
    def enterData(self, webelement, data):
        webelement.send_keys(data)

    def buttonClick(self, webelement):
        self.driver.execute_script("arguments[0].click();", webelement)

    def switchToFrame(self, frame):
        self.driver.switch_to.frame(frame)

    def ActionChains(self):
        a = ActionChains(self.driver)
        return a

    def selectDropdown(self, dropdown, data_to_select):
        s = Select(dropdown)
        options = s.options
        for option in options:
            option_value = option.text
            if option_value == data_to_select:
                option.click()
                break

    def selectYear(self, year_header, year_to_select, next_button):
        while year_header.text != year_to_select:
            self.buttonClick(next_button)

    def selectMonth(self, months, data_to_select):
        for month in months:
            if month.text == data_to_select and month.get_attribute("class") == "month":
                self.buttonClick(month)
                break

    def selectDate(self, dates, date_to_select):
        for date in dates:
            date_value = date.text
            if date_value == date_to_select and date.get_attribute("class") == "day":
                self.buttonClick(date)
                break

    def selectCheckbox(self, checkboxs, data_to_select):
        i = 1
        j = 0

        while i <= len(data_to_select):
            if checkboxs[j].text in data_to_select:
                self.buttonClick(checkboxs[j].find_element(By.XPATH, "parent::tr/td[1]/input"))
                i = i + 1
            j = j + 1

    def getDropdownValues(self, dropdown):
        s = Select(dropdown)
        list = []
        for option in s.options:
            value = option.text
            if "Select" not in value:
                list.append(value)

        return list
