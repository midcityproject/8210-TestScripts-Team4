import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Edit_Investment(unittest.TestCase):
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

        time.sleep(3)
        driver.get("http://efsblog3.herokuapp.com/investment/")
        time.sleep(3)
        driver.get("http://efsblog3.herokuapp.com/investment/13/edit")
        time.sleep(3)

        recent_value = "11555"

        elem = driver.find_element_by_id("id_recent_value")
        elem.clear()
        elem.send_keys(recent_value)
        time.sleep(5)
        elem = driver.find_element_by_css_selector("button.save.btn.btn-default").click()
        time.sleep(3)
        driver.get("https://efsblog3.herokuapp.com/investment/")
        assert "recent_value in Investment Edited"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

