import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Midcity_Emp_Edit_Event(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log(self):
        user = "klumbard"
        pwd = "School_6"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000/")
        assert "Logged In"
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/manage_activity/")
        time.sleep(5)
        driver.get("http://127.0.0.1:8000/manage_activity/1222345/edit_event/")
        time.sleep(5)
        ########Test Data########
        organization = "Foodbank for the Heartland"
        type = "Food Donation"
        location = "Omaha NE"
        short_description = "Sorting and boxing up donated food."
        description = "Sorting and boxing up donated food and Sorting and boxing up donated food.and Sorting and boxing up donated food and Sorting and boxing up donated food and Sorting and boxing up donated food."
        start_date = "2017-11-03"
        ttime = "9:00 AM"
        number_volunteers= "10"
        ##########################
        elem = driver.find_element_by_name("organization")
        elem.clear()
        elem.send_keys(organization)
        elem = driver.find_element_by_name("type")
        elem.clear()
        elem.send_keys(type)
        elem = driver.find_element_by_name("location")
        elem.clear()
        elem.send_keys(location)
        elem = driver.find_element_by_name("short_description")
        elem.clear()
        elem.send_keys(short_description)
        elem = driver.find_element_by_name("description")
        elem.clear()
        elem.send_keys(description)
        elem = driver.find_element_by_name("start_date")
        elem.clear()
        elem.send_keys(start_date)
        elem = driver.find_element_by_name("time")
        elem.clear()
        elem.send_keys(ttime)
        elem = driver.find_element_by_name("number_volunteers")
        elem.clear()
        elem.send_keys(number_volunteers)
        time.sleep(5)
        elem = driver.find_element_by_css_selector("button.btn.btn-success.btn-raised").click()
        time.sleep(1)
        driver.get("http://midcityproject.pythonanywhere.com/manage_activity/")
        time.sleep(1)
        assert "Edited Customer"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()