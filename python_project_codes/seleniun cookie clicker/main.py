from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

PATH = "/home/rammani/Downloads/chromedriver"
URL = "https://www.python.org/"

s = Service(executable_path=PATH)  # creates a service/instance of chrome to pass to webdriver
driver = webdriver.Chrome(service=s)
driver.get(URL)

event_dict = {}

# my way to find time and event

i = 0
element = driver.find_element(By.CLASS_NAME, "event-widget")
event_list = element.find_elements(By.TAG_NAME, "li")
for event in event_list:
    time = event.find_element(By.TAG_NAME, "time")
    time = time.get_attribute("datetime").split("T")[0]
    title = event.find_element(By.TAG_NAME, "a").text
    new_event = {"time": f"{time}", "event": title}
    event_dict[f"{i}"] = new_event
    i += 1

# # teacher's way
# times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

print(event_dict)
