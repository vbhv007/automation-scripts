#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import re

regno = "add your regno"
passwd = "add your password"
CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver'
WINDOW_SIZE = "1920,1080"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)
  
driver.get("http://172.20.72.15/customer_portal")
driver.find_element_by_id('auth_user').send_keys(regno)
driver.find_element_by_id('auth_pass').send_keys(passwd)
driver.find_element_by_id("accept").click()
time.sleep(1)
tds = driver.find_elements_by_tag_name("td")
for i in tds:
	if(re.findall(r'Data quota in vendor' , i.text)):
		print(i.text)
		break
driver.close()
