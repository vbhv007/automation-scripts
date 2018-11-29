#!/usr/bin/python3

from datetime import timedelta
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import datetime
import random

def get_reason():
	reasons = ['Shopping', 'Haicut', 'Food']
	i = random.randrange(0, 3)
	return reasons[i] 

def get_place():
	places = ['Kellambakam', 'Vandaloor', 'Kandigai', 'Tambaram']
	j = random.randrange(0, 4)
	return places[j]

def outing_date():
	increment = 5 - datetime.date.today().weekday()
	outing = (datetime.date.today() + timedelta(days=increment))
	return outing.strftime('%d-%b-%Y')


if __name__ == '__main__':
	regno = "your_reg_number"
	passwd = "your_password"
	next_sunday = outing_date()
	place = get_place()
	reason = get_reason()
	smobile = 'apna number daal de'
	pmobile = 'papa ka number daal de'
	facmobile = 'proctor ka bhi daal de'
	browser = webdriver.Chrome() ## or you can use firefox
	browser.get("https://academicscc.vit.ac.in/student/")
	browser.find_element_by_name("regno").send_keys(regno)
	browser.find_element_by_name("passwd").send_keys(passwd)

	## TODO: Add auto captcha
	while True:
		if len(browser.find_element_by_name("vrfcd").get_attribute("value")) == 6:
			break

	browser.find_element_by_class_name("submit3").click()
	WebDriverWait(browser, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
	browser.get("https://academicscc.vit.ac.in/student/outing.asp")
	WebDriverWait(browser, 10).until(lambda d: d.execute_script('return document.readyState') == 'complete')
	browser.find_element_by_xpath("//select[@name='apply']/option[@value='50174']").click()
	time.sleep(1)
	browser.find_element_by_id("demo32").send_keys(next_sunday)
	browser.find_element_by_xpath("//select[@name='sttime_hh']/option[@value='09']").click()
	browser.find_element_by_xpath("//select[@name='sttime_mm']/option[@value='00']").click()
	browser.find_element_by_xpath("//input[@name='frm_timetype' and @value='AM']").click()
	browser.find_element_by_xpath("//select[@name='endtime_hh']/option[@value='06']").click()
	browser.find_element_by_xpath("//select[@name='endtime_mm']/option[@value='00']").click()
	browser.find_element_by_xpath("//input[@name='to_timetype' and @value='PM']").click()
	browser.find_element_by_name("place").send_keys(place)
	browser.find_element_by_name("reason").send_keys(reason)
	browser.find_element_by_name("smobile").send_keys(smobile)
	browser.find_element_by_name("pmobile").send_keys(pmobile)
	browser.find_element_by_name("facmobile").send_keys(facmobile)
	browser.find_element_by_name("requestcmd").click()
	time.sleep(3) ## just a precaution
	print("Leave Applied")
	browser.close()

