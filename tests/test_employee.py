import pytest
from assertpy import assert_that
from selenium.webdriver.common.by import By

from base.webdriver_listener import WebDriverWrapper
from utilities import data_source


class TestAddEmployee(WebDriverWrapper):

    @pytest.mark.parametrize(
        "username, password, firstname, middlename, lastname, expected_profile_header,expected_firstname",
        data_source.test_add_valid_employee_data
    )
    def test_add_valid_employee(self, username, password, firstname, middlename, lastname, expected_profile_header,
                                expected_firstname):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.driver.find_element(By.XPATH, "//span[normalize-space()='PIM']").click()
        self.driver.find_element(By.LINK_TEXT, "Add Employee").click()
        self.driver.find_element(By.NAME, "firstName").send_keys(firstname)
        self.driver.find_element(By.NAME, "middleName").send_keys(middlename)
        self.driver.find_element(By.NAME, "lastName").send_keys(lastname)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

        actual_profile_header = self.driver.find_element(By.XPATH,
                                                         f"//h6[contains(normalize-space(),'{firstname}')]").text
        actual_first_name = self.driver.find_element(By.NAME, "firstName").get_attribute("value")

        assert_that(expected_profile_header).is_equal_to(actual_profile_header)
        assert_that(expected_firstname).is_equal_to(actual_first_name)

