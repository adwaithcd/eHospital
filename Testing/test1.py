from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
browser = webdriver.Firefox()
home_page = 'http://localhost/hospital/admin/'
login_page = 'http://localhost/hospital'
browser.get( "http://localhost/hospital ")
  
username = browser.find_element_by_id( "user" )
password = browser.find_element_by_id( "pass" )
submit   = browser.find_element_by_id( "submit"   )
  
username.send_keys( "admin" )
password.send_keys( "admin" )
  

submit.click()


wait = WebDriverWait( browser, 5 )
  
try:
	page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
except TimeoutException:
	print( "Loading timeout expired" )
  
assert (browser.current_url == home_page),"Failed Login"
print("Successful")
browser.close()