import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "/home/rammani/Downloads/chromedriver"
URL = "https://secure-retreat-92358.herokuapp.com/"
s = Service(executable_path=PATH)
driver = webdriver.Chrome(service=s)

driver.get(URL)

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("myFName")

lname = driver.find_element(By.NAME, "lName")
lname.send_keys("MyLName")

email = driver.find_element(By.NAME, "email")
email.send_keys("ajksa@jskdf")
email.send_keys(Keys.ENTER)

time.sleep(7)