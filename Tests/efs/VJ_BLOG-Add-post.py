from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class blogtest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "vjampani"
        pwd = "Vijay123"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://msda1p1.herokuapp.com/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://msda1p1.herokuapp.com/")
        assert "Logged In"
        time.sleep(5)
        driver.get("https://msda1p1.herokuapp.com/post/new/")
        time.sleep(5)
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("vjampani - Test")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("This post is created as a test")
        time.sleep(5)
        elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
        time.sleep(5)
        assert "Posted Blog Entry"

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
   unittest.main()