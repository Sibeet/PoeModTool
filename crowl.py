import sys
from selenium import webdriver
from enum import Enum

class ItemType(Enum):
    Claws = "Claw"

def get_connection():
    chromedriver = "./chromedriver.exe"

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('disable-gpu')

    driver = webdriver.Chrome(chromedriver, options=option)
    return driver

def get_modifier(driver, item_category, item_type):
    driver.get("https://poedb.tw/us/mod.php?cn=One%20Hand%20Sword")

    canvas = driver.find_element_by_xpath('//*[@id="canvas"]')

i = 1
mod_type_list = []
while(True):
    try:
        mod_type_list.append(canvas.find_element_by_xpath(F'./div[{i}]'))
        i= i+1
    except:
        break