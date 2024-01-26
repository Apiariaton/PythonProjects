from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys 
import pandas as pd


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
number_of_wikipedia_articles = driver.find_element(By.CSS_SELECTOR,value="div#articlecount a")
same_number = driver.find_element(By.XPATH,value='//*[@id="articlecount"]/a[1]')





print(number_of_wikipedia_articles,same_number)
# number_of_wikipedia_articles.click()

search_bar = driver.find_element(By.NAME,value="search")
search_bar.send_keys("Python",Keys.ENTER)


driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME,value="fName")
first_name.send_keys("William")
last_name = driver.find_element(By.NAME,value="lName")
last_name.send_keys("Holder")
email_address = driver.find_element(By.NAME,value="email")
email_address.send_keys("wholder321@gmail.com",Keys.ENTER)