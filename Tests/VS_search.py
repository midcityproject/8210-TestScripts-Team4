import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
class Midcity_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin/")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       time.sleep(3)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(5)
       # Login button is clicked
       elem.send_keys(Keys.RETURN)
       time.sleep(5)
       assert "Logged In"
       # goes to user page
       driver.get("http://127.0.0.1:8000/admin/auth/user/")
       time.sleep(5)
       assert "Inside Users Page"
       driver.find_element_by_xpath("/html/body[@class=' app-auth model-user change-list']/div[@id='container']/div[@id='content']/div[@id='content-main']/div[@id='changelist']/div[@id='toolbar']/form[@id='changelist-search']/div/input[@id='searchbar']").clear()
       elem = driver.find_element_by_xpath("/html/body[@class=' app-auth model-user change-list']/div[@id='container']/div[@id='content']/div[@id='content-main']/div[@id='changelist']/div[@id='toolbar']/form[@id='changelist-search']/div/input[@id='searchbar']")
       elem.send_keys("vaishnavi")
       #search button is clicked
       elem = driver.find_element_by_xpath("/html/body[@class=' app-auth model-user change-list']/div[@id='container']/div[@id='content']/div[@id='content-main']/div[@id='changelist']/div[@id='toolbar']/form[@id='changelist-search']/div/input[2]").click()
       time.sleep(5)
       assert "Search results are produced"
       driver.get("http://127.0.0.1:8000/admin/")
       time.sleep(5)


   def tearDown(self):
       self.driver.close()



if __name__ == "__main__":
   unittest.main()