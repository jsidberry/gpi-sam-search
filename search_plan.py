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


class Wireplan:    
    
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
        # stevens_pt_pumps_qam_groups_url = self.stevens_pt_pumps_qam_groups_url
        # driver.get(stevens_pt_pumps_qam_groups_url)
        
        # wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
        #                                                    ElementNotVisibleException,
        #                                                    ElementNotSelectableException])
        # # element = wait.until(EC.element_to_be_clickable(by_type, locator))
        
        # print("Search Options...")
        # print("")
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='page-search']//form[@class='page-search']//div[@class='page-search-box']//p[@class='search']/a")))
        # element.click()
        
        time.sleep(7)
        driver.quit()

        
ff = Wireplan()
ff.login_process()   # User login

