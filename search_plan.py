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
		self.signin_url = "http://mdms-settings.charter.com:8300/operators/sign_in"
		self.base_url = "http://mdms-settings.charter.com:8300/"
		self.user_email_address = ""
		self.user_password = ""
		
		
	def login_process(self):
		print("Opening browser and logging in...")
		driver = self.driver
		user_email_address = self.user_email_address
		user_password = self.user_password
		self.driver.get(self.signin_url)
		wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
														   ElementNotVisibleException,
														   ElementNotSelectableException])
		# element = wait.until(EC.element_to_be_clickable(By.XPATH , locator))
		driver.find_element(By.XPATH, "//header/section/article/ul/li/a").click()
		driver.find_element(By.XPATH, "//form[@id='new_operator']//input[@id='operator_email']").send_keys(user_email_address)
		# driver.find_element(By.ID, "operator_password").send_keys(user_password)
		element = wait.until(EC.presence_of_element_located((By.ID, "operator_password")))
		element.send_keys(user_password)
		driver.find_element(By.XPATH, "//form[@id='new_operator']//input[@name='commit']").click()
	
	
	def get_csv_data(filename):
		# create an empty list to store rows
		rows = []
		
		# open the CSV file
		data_file = open(filename, "r")
		
		# create a CSV reader from CSV file
		csv_reader = csv.reader(data_file)
		
		# skip the header
		next(reader)
		
		# add rows from reader to list
		for row in csv_reader:
			rows.append(row)
			
		return rows
	
	
	def test(self):
		driver = self.driver
		# driver.maximize_window()
				
		print("Stevens-Point QAM Group URL...")
		print("")
		stevens_pt_pumps_qam_groups_url = self.stevens_pt_pumps_qam_groups_url
		driver.get(stevens_pt_pumps_qam_groups_url)
		
		wait = WebDriverWait(self.driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,
														   ElementNotVisibleException,
														   ElementNotSelectableException])
		# element = wait.until(EC.element_to_be_clickable(by_type, locator))
		
		print("Search Options...")
		print("")
		element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='page-search']//form[@class='page-search']//div[@class='page-search-box']//p[@class='search']/a")))
		element.click()
		
		print("Enter search value...")
		print("")
		search_value = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='search_name']")))
		search_value.send_keys("*172.17.81.161*") # this value will come fro a CSV file. TODO: load data from CSV into list/dict/tuple
		stevens_pt_current_url = driver.current_url
		
		print("Clicking Search button...")
		print("")
		blue_search_button = driver.find_element(By.XPATH, "//div[@id='headends_qam_groups']//form[@action='/qrm/regions/sldcmo-ndc2/headends/stevens-pt-fsm/qam_groups']/div[2]/div/div/div[2]/a[1]")
		blue_search_button.click()
		driver.implicitly_wait(5)
		
		print("Click 1st link on resulting list...")
		print("")
		first_link_in_table = driver.find_element(By.XPATH, "//table[@id='qam_groups']//a[1]")
		first_link_in_table.click()
		driver.implicitly_wait(5)
		
		print("Search Options...")
		print("")
		driver.find_element(By.XPATH, "//p[@class='search']/a[@href='#']").click()
		driver.implicitly_wait(5)
		
		print("Enter search value...")
		print("")
		search_value = driver.find_element(By.XPATH, "//input[@id='search_name']")
		search_value.send_keys("*46005Q1*") # this value will come fro a CSV file. TODO: load data from CSV into list/dict/tuple
		driver.implicitly_wait(5)
		
		print("Clicking BLUE Search button...")
		print("")
		blue_search_button = driver.find_element(By.XPATH, "/html/body/div/section/section[2]/article/dl/dd[4]/div/div/div[6]/div/form/div[2]/div/div/div[2]/a[1]")
		blue_search_button.click()
		driver.implicitly_wait(5)
		
		time.sleep(7)
		driver.quit()

		
ff = Wireplan()
ff.login_process()   # User login

