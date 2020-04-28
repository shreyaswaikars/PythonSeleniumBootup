import unittest
import openpyxl
from builtins import classmethod
# from webDriverUtility import supplydriver
from webDriverUtility import supplyDriver

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = supplyDriver("chrome")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://demowebshop.tricentis.com/")

    @classmethod
    def tearDownClass(self):
        self.driver.close()

    def login(self, Email, Password):
        self.driver.find_element_by_id("Email").send_keys(Email)
        self.driver.find_element_by_id("Password").send_keys(Password)
        self.driver.find_element_by_css_selector("input[value='Log in']").click()
        loginname = self.driver.find_element_by_class_name("account").text
        if loginname == Email:
            self.driver.find_element_by_link_text("Log out").click()
            self.driver.find_element_by_link_text("Log in").click()
            return "Valid User"
        else:
            self.driver.find_element_by_id("Email").clear()
            self.driver.find_element_by_id("Password").clear()
            return "Invalid User"

    def test1_LoginData(self):
        self.driver.find_element_by_link_text("Log in").click()
        file_path = r"test-data/Test_Data-demowebshop.xlsx"
        wb = openpyxl.load_workbook(file_path)
        Sheet1 = wb["Sheet1"]
        for c1, c2, c3 in Sheet1['A2:C3']:
            c3.value = self.login(c1.value, c2.value)
        wb.save(file_path)
        wb.close()