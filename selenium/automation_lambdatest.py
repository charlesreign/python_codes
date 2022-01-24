from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_browser = webdriver.Firefox()

firefox_browser.maximize_window()

firefox_browser.get('https://accounts.lambdatest.com/register')

# checking if Signup for Free can be found on the page
assert 'Signup for Free' in firefox_browser.page_source

# fullname = firefox_browser.find_element_by_name('name')
fullname = firefox_browser.find_element(By.NAME, 'name')
fullname.clear()
# business_email = firefox_browser.find_element_by_name('email')
business_email = firefox_browser.find_element(By.NAME, 'email')
business_email.clear()
# password = firefox_browser.find_element_by_id('userpassword')
password = firefox_browser.find_element(By.ID, 'userpassword')
password.clear()
# phone = firefox_browser.find_element_by_name('phone')
phone = firefox_browser.find_element(By.NAME, 'phone')
phone.clear()

fullname.send_keys("Charles Reign")
business_email.send_keys("charliereign@email.com")
password.send_keys("password")
phone.send_keys("+233 24 123 4567")
