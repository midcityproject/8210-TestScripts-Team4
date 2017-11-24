import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EFS_Test_Investment(unittest.TestCase):

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
        driver.get("http://klumbard.pythonanywhere.com/investment/")
        time.sleep(5)
        elem = driver.find_element_by_css_selector("span.btn.btn-primary").click()
        time.sleep(5)
        ########Test Data########
        id_customer = "12056"
        category = "test category"
        description = "Test description"
        acquired_value= "5000"
        acquired_date = "2012-11-24"
        recent_value = "5010"
        recent_date = "2017-11-24"
        ##########################
        elem = driver.find_element_by_id("id_customer")
        elem.send_keys(id_customer)
        elem = driver.find_element_by_id("id_category")
        elem.send_keys(category)
        elem = driver.find_element_by_id("id_description")
        elem.send_keys(description)
        elem = driver.find_element_by_id("id_acquired_value")
        elem.send_keys(acquired_value)
        elem = driver.find_element_by_id("id_acquired_date")
        elem.clear()
        elem.send_keys(acquired_date)
        elem = driver.find_element_by_id("id_recent_value")
        elem.send_keys(recent_value)
        elem = driver.find_element_by_id("id_recent_date")
        elem.clear()
        elem.send_keys(recent_date)
        time.sleep(5)
        elem = driver.find_element_by_css_selector("button.save.btn.btn-default").click()
        time.sleep(5)
        assert "Added New Investment"
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()