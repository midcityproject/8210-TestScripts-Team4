import csv
import time
import datetime
import unittest



from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Midcity_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
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

       assert "Logged In"
       time.sleep(5)
       driver.get("http://127.0.0.1:8000/admin/volunteer_activity/event/")
       time.sleep(7)
       driver.get("http://127.0.0.1:8000/admin/volunteer_activity/event/add/")
       time.sleep(5)
       assert "Inside Event adding Page"
       count = 1
       with open('addEvents.csv') as csvfile:
           data = csv.reader(csvfile, delimiter=',')
           for row in data:

               if (count  != 1):
                   event_num = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-event_num']/div/input[@id='id_event_num']")
                   event_num.send_keys(row[0])
                   org = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-organization']/div/input[@id='id_organization']")
                   org.send_keys(row[1])
                   type = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-type']/div/input[@id='id_type']")
                   type.send_keys(row[2])
                   location = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-location']/div/input[@id='id_location']")
                   location.send_keys(row[3])
                   description = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-description']/div/input[@id='id_description']")
                   description.send_keys(row[4])
                   s_description = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-short_description']/div/input[@id='id_short_description']")
                   s_description.send_keys(row[5])
                   num_vol = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-number_volunteers']/div/input[@id='id_number_volunteers']")
                   num_vol.send_keys(row[6])
                   status = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-status']/div/input[@id='id_status']")
                   status.send_keys(row[7])
                   event_time = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/fieldset[@class='module aligned ']/div[@class='form-row field-time']/div/input[@id='id_time']")
                   event_time.send_keys(row[8])
                   submit = driver.find_element_by_xpath("/html/body[@class=' app-volunteer_activity model-event change-form']/div[@id='container']/div[@id='content']/div[@id='content-main']/form[@id='event_form']/div/div[@class='submit-row']/input[2]").click()
               count = count + 1

       driver.get("http://127.0.0.1:8000/admin/volunteer_activity/event/")
       time.sleep(7)




   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()