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
        time.sleep(2)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(username)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(password)
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        driver.get("http://midcityproject.pythonanywhere.com/")
        assert "Logged In"
        time.sleep(5)
        driver.get("http://midcityproject.pythonanywhere.com/manage_activity/")
        time.sleep(1)
        driver.get("http://midcityproject.pythonanywhere.com/manage_activity/create/")
        time.sleep(5)

        hours= "25"
        elem = driver.find_element_by_xpath("//select[@name='user_num']/option[text()='instructor']").click()
        elem = driver.find_element_by_xpath("//select[@name='event_num']/option[text()='100']").click()
        elem = driver.find_element_by_id("id_hours")
        elem.send_keys(hours)
        time.sleep(5)
        elem = driver.find_element_by_css_selector("button.save.btn.btn-raised.btn-success").click()
        time.sleep(1)
        driver.get("http://midcityproject.pythonanywhere.com/manage_activity/")
        time.sleep(1)
        assert "Volunteer Activity Added"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

