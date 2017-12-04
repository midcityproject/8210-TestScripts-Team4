import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EFS_Test_Stock(unittest.TestCase):

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
        driver.get("http://klumbard.pythonanywhere.com/stock/")
        time.sleep(5)
        driver.get("http://klumbard.pythonanywhere.com/stock/14/delete")
        time.sleep(5)
        assert "Deleted stock"
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()