from __future__ import print_function
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from wait_type.explicit_wait_type import ExplicitWaitType
import time
import csv
# from lxml import html


class SearchPlan:    
    
    def __init__(self):
        self.driver = driver = webdriver.Firefox()
        self.signin_url = "https://samdaily.us/fbo/fbosearch.html"
        self.base_url = "https://samdaily.us/fbo/fbosearch.html"
        self.user_email_address = ""
        self.user_password = ""
    
    
    def test(self):
        driver = self.driver
        # driver.maximize_window()
                
        print("Basic Search...")
        print("")
        
        time.sleep(3)
        driver.quit()

        
ff = SearchPlan()
ff.test()

