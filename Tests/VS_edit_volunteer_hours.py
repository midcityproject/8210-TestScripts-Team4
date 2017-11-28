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
       driver.get("http://127.0.0.1:8000/accounts/login/")
       #Username Textbox
       elem = driver.find_element_by_xpath("/html/body/div[@class='container col-sm-6']/div[@class='row']/div[@class='col']/div[@class='form-group']/form/div[@class='form-group'][1]/input[@id='<input type=']")
       elem.send_keys(user)
       time.sleep(5)
       #Password Textbox
       elem = driver.find_element_by_xpath("/html/body/div[@class='container col-sm-6']/div[@class='row']/div[@class='col']/div[@class='form-group']/form/div[@class='form-group'][2]/input[@id='<input type=']")
       elem.send_keys(pwd)
       time.sleep(5)
       # Hit Enter
       elem.send_keys(Keys.RETURN)
       # Go to Home Page
       driver.get("http://127.0.0.1:8000")
       assert "Logged In"
       time.sleep(5)
       assert "Currently at Index"
       # Click the 'Track My Hours' button
       elem = driver.find_element_by_xpath("/html/body/div[@class='container']/div[@class='col text-center'][2]/a[@class='btn btn-raised btn-info center-block']").click()
       time.sleep(5)
       assert "Currently at Track my Hours Page"
       # Click the 'Edit Hours' button
       elem = driver.find_element_by_xpath("/html/body/div[@class='container']/div[@class='row']/div[@id='link-tags']/table[@class='table table-bordered table-inverse']/tbody/tr[@class='bg-dark']/td[4]/a[@class='btn btn-warning']").click()
       time.sleep(5)
       assert "Currently at Editing Page"
       # Clear the Hours TextField
       driver.find_element_by_xpath("/html/body/form[@class='userevent-form']/p[2]/input[@id='id_hours']").clear()
       # Set Hours
       elem = driver.find_element_by_xpath("/html/body/form[@class='userevent-form']/p[2]/input[@id='id_hours']")
       elem.send_keys(randint(1, 9))
       time.sleep(7)
       assert "Setting Volunteer Hours"
       # Click Update
       elem = driver.find_element_by_xpath("/html/body/form[@class='userevent-form']/button[@class='save btn btn-default']").click()
       time.sleep(7)
       # Navigate back to Home Page
       driver.get("http://127.0.0.1:8000")
       time.sleep(7)


   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()

