from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options = chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(3)
accept_cookies = driver.find_element(By.CSS_SELECTOR,value="button.fc-button.fc-cta-consent.fc-primary-button")
accept_cookies.click()

driver.implicitly_wait(2)
select_English_as_language = driver.find_element(By.CSS_SELECTOR,value="#langSelect-EN")
select_English_as_language.click()

driver.implicitly_wait(2)
bakery_name = driver.find_element(By.CSS_SELECTOR,"#bakeryName")
bakery_name.click()

bakery_name_input_field = driver.find_element(By.CSS_SELECTOR,"#bakeryNameInput")
bakery_name_input_field.send_keys("Will's Boulangerie",Keys.ENTER)
driver.implicitly_wait(2)

cookie = driver.find_element(By.CSS_SELECTOR,value="#bigCookie")
timeToEndCookieClicking = time.time() + (60 * 5)

timeInFiveSecondsTime = time.time() + 5
while True:
    cookie.click()
    timeNow = time.time()
    if timeNow > timeToEndCookieClicking:
        break
    elif timeNow > timeInFiveSecondsTime:
        try:
            available_upgrades = driver.find_elements(By.CSS_SELECTOR,value=".product.unlocked.enabled")
            most_expensive_available_upgrade = available_upgrades[len(available_upgrades)-1]
            most_expensive_available_upgrade.click()
        except Exception as e:
            print(e)
            print("No upgrade available for purchase")
        timeInFiveSecondsTime = time.time() + 5

