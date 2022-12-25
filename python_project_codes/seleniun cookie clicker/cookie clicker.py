import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = "/home/rammani/Downloads/chromedriver"
URL = "https://orteil.dashnet.org/experiments/cookie/"
s = Service(executable_path=PATH)
driver = webdriver.Chrome(service=s)
driver.get(URL)


def choose_item(current_money, items, prices):
    index = 0
    for price in prices:
        if current_money > price:
            index = prices.index(price)
    return items[index]


def integer(value: str) -> int:
    var = int(value.replace(",", ""))
    return var


cookie = driver.find_element(By.ID, "cookie")

timeout_end = time.time() + 300
five_sec_end = time.time() + 5
should_buy = False


def buy():
    cursor = driver.find_element(By.ID, "buyCursor")
    grandma = driver.find_element(By.ID, "buyGrandma")
    factory = driver.find_element(By.ID, "buyFactory")
    mine = driver.find_element(By.ID, "buyMine")
    shipment = driver.find_element(By.ID, "buyShipment")
    alchemy = driver.find_element(By.ID, "buyAlchemy lab")
    portal = driver.find_element(By.ID, "buyPortal")
    time_machine = driver.find_element(By.ID, "buyTime machine")
    
    money = integer(driver.find_element(By.ID, "money").text)
    cursor_price = integer(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split()[2])
    grandma_price = integer(driver.find_element(By.CSS_SELECTOR, "#buyGrandma b").text.split()[2])
    factory_price = integer(driver.find_element(By.CSS_SELECTOR, "#buyFactory b").text.split()[2])
    mine_price = integer(driver.find_element(By.CSS_SELECTOR, "#buyMine b").text.split()[2])
    shipment_price = integer(driver.find_element(By.CSS_SELECTOR, "#buyShipment b").text.split()[2])
    alchemy_price = integer(driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.split()[3])
    portal_price = integer(driver.find_element(By.CSS_SELECTOR, "#buyPortal").text.split()[2])
    time_machine_price = integer(driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.split()[3])
    
    item_list = [cursor, grandma, factory, mine, shipment, alchemy, portal, time_machine]
    price_list = [cursor_price, grandma_price, factory_price, mine_price, shipment_price, alchemy_price,
                  portal_price, time_machine_price]
    
    buy_item = choose_item(money, item_list, price_list)
    buy_item.click()


i = 1
# while time.time() < timeout_end:
while True:
    cookie.click()
    time.sleep(0.00001)
    
    if time.time() > five_sec_end:
        buy()
        
        five_sec_end = time.time() + i
        i += 1
