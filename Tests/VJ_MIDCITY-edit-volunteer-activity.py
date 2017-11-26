from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class test1(unittest.TestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome()

    def test_midcity(self):
        username = "midcityproject"
        password = "Team4MSD"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://midcityproject.pythonanywhere.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(username)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)
        driver.get("http://midcityproject.pythonanywhere.com/")
        assert "Logged In"
        time.sleep(5)
        driver.get("http://midcityproject.pythonanywhere.com/manage_activity/")
        time.sleep(5)
        driver.get("http://midcityproject.pythonanywhere.com/manage_activity/47/edit/")
        time.sleep(5)

        hours= "10"

        elem = driver.find_element_by_id("id_hours")
        elem.clear()
        elem.send_keys(hours)
        time.sleep(5)
        elem = driver.find_element_by_css_selector("button.save.btn.btn-default").click()
        time.sleep(5)
        driver.get("http://midcityproject.pythonanywhere.com/manage_activity/")
        time.sleep(5)
        assert "Volunteer Activity Edited"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

