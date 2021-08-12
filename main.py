from splinter.browser import Browser
from selenium import webdriver 
from selenium.webdriver import ActionChains
import time

url = "https://popcat.click/"
#Your geckodriver address
addressOfGeckodriver = '(Your address)'

string = ['\n']*800

driver = webdriver.Firefox(executable_path = addressOfGeckodriver) 
driver.get(url)

while(True):
    ActionChains(driver).move_to_element(driver.find_element_by_id("app")).send_keys(string).perform()
    #In order to prevent cat's eyes be red.
    time.sleep(30.0)
    
    
#Made by Wang Shao-Lei
