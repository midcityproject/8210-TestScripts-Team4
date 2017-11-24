import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EFS_Test_Customer(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log(self):
        user = "klumbard"
        pwd = "School_6"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://klumbard.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://klumbard.pythonanywhere.com")
        assert "Logged In"
        time.sleep(5)
        driver.get("http://klumbard.pythonanywhere.com/customer/")
        time.sleep(5)
        driver.get("http://klumbard.pythonanywhere.com/customer/1/edit")
        time.sleep(5)
        ########Test Data########
        cust_number = "12056"
        name = "Katherine M McClusky"
        address = "6782 Mile High Street"
        city = "Denver"
        state = "CO"
        zipcode = "69129"
        email = "katherinemc@gmail.com"
        cell_phone = "515-554-3499"
        ##########################
        elem = driver.find_element_by_id("id_cust_number")
        elem.clear()
        elem.send_keys(cust_number)
        elem = driver.find_element_by_id("id_name")
        elem.clear()
        elem.send_keys(name)
        elem = driver.find_element_by_id("id_address")
        elem.clear()
        elem.send_keys(address)
        elem = driver.find_element_by_id("id_city")
        elem.clear()
        elem.send_keys(city)
        elem = driver.find_element_by_id("id_state")
        elem.clear()
        elem.send_keys(state)
        elem = driver.find_element_by_id("id_zipcode")
        elem.clear()
        elem.send_keys(zipcode)
        elem = driver.find_element_by_id("id_email")
        elem.clear()
        elem.send_keys(email)
        elem = driver.find_element_by_id("id_cell_phone")
        elem.clear()
        elem.send_keys(cell_phone)
        time.sleep(5)
        elem = driver.find_element_by_css_selector("button.save.btn.btn-default").click()
        time.sleep(5)
        assert "Edited Customer"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()