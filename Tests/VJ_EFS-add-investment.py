import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Add_Investment(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log(self):
        user = "vjampani"
        pwd = "Vijay123"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://efsblog3.herokuapp.com/admin/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://efsblog3.herokuapp.com/")
        assert "Logged In"

        driver.get("https://efsblog3.herokuapp.com/investment/")
        time.sleep(5)
        elem = driver.find_element_by_css_selector("span.btn.btn-primary").click()
        time.sleep(5)

        id_customer = "12056"
        category = "Testing"
        description = "Sample text added here as description"
        acquired_value = "11222"
        acquired_date = "2017-10-22"
        recent_value = "22333"
        recent_date = "2017-11-26"
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
        time.sleep(3)
        driver.get("https://efsblog3.herokuapp.com/investment/")
        assert "New Investment added"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

