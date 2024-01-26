from selenium import webdriver
from selenium.webdriver.common.by import By



chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://www.google.com/search?gs_ssp=eJzj4tVP1zc0zKgqT65KycgzYPSSL8lIVUjJTCyqVMhPU0hUqMwvzUtXyEssKS1KzMksLgEAiiIQ8g&q=the+diary+of+a+young+naturalist&oq=the+diary+of+a+young+&gs_lcrp=EgZjaHJvbWUqBwgBEC4YgAQyBggAEEUYOTIHCAEQLhiABDIHCAIQABiABDIHCAMQLhiABDIGCAQQRRhA0gEINDQ2NmowajSoAgCwAgA&sourceid=chrome&ie=UTF-8")

reject_cookies_button = driver.find_element(By.CSS_SELECTOR,value="button#W0wltc")
reject_cookies_button.click()

first_link = driver.find_element(By.CSS_SELECTOR,value="span a").get_attribute("href")
print(first_link)

price_element = driver.find_element(By.CSS_SELECTOR,value="div.RRDLx div.i3YBTb div.qptdjc").text
print(price_element)