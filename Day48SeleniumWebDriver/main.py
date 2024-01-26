from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd


#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)



driver = webdriver.Chrome(options=chrome_options)
driver.get("https://blackwells.co.uk/bookshop/category/_top")

#Reject cookies
reject_cookie_button = driver.find_element(by=By.CSS_SELECTOR,value="button#onetrust-reject-all-handler")
reject_cookie_button.click()

book_units = driver.find_elements(by=By.CSS_SELECTOR,value="div.product-info")
book_titles = []
book_prices = []

for unit in book_units:
    book_title = unit.find_element(by=By.CSS_SELECTOR,value="h4 a").text
    book_titles.append(book_title)
    try:
        book_price = unit.find_element(by=By.CSS_SELECTOR,value="li.product-price--current").text
        book_prices.append(book_price.replace("£",""))
    except Exception as e:
        print("No price found for this book...")
        book_prices.append(0)

for title in book_titles:
    print(title)

for price in book_prices:
    print(price)

print("Number of book titles",len(book_titles))
print("Number of price labels",len(book_prices))

price_comparison_table = {"Book Title": book_titles, "Price on Blackwells": book_prices}
df = pd.DataFrame(data = price_comparison_table)
print(df.head())

# :nth-child(n)	p:nth-child(2)	Selects every <p> element that is the second child of its parent
driver.implicitly_wait(5)
driver.implicitly_wait(5)
driver.get("https://www.google.com/")
driver.implicitly_wait(5)

#Reject cookies
reject_cookies_button = driver.find_element(By.XPATH,value='//*[@id="W0wltc"]')
reject_cookies_button.click()

driver.get("https://www.google.com/")
search_bar = driver.find_element(By.CSS_SELECTOR,value="textarea")
search_bar.send_keys(book_titles[0])
search_bar.send_keys(Keys.ENTER)
driver.implicitly_wait(0.7)
book_prices_elsewhere = driver.find_elements(By.CSS_SELECTOR,value="div.RRDLx")
this_book_price = driver.find_element(By.XPATH,value='//html/body/div[14]/div/div/div[1]/a/div[3]/div[2]/div/div').text
print(this_book_price)
for book in book_prices_elsewhere:
    print(book.text)



#Get search bar
# for book in book_titles:
#     driver.get("https://www.google.com/")
#     search_bar = driver.find_element(By.CSS_SELECTOR,value="textarea")
#     search_bar.send_keys(book)
#     search_bar.send_keys(Keys.ENTER)
#     driver.implicitly_wait(0.7)
#     #book_prices_elsewhere = driver.find_elements(By.CSS_SELECTOR,value="div.pla-hovercard-content-ellip div:nth-child(2) a div:nth-child(3) div:nth-child(2) div div")
#     book_prices_elsewhere = driver.find_elements(By.CSS_SELECTOR,value="div.RRDLx div div")

#     for price in book_prices_elsewhere:
#         print(price.text)

#     driver.implicitly_wait(5)

#vplahcl_ou6vZfi3EKmUhbIPiqqzuAk_39ou6vZdC0FeqlwuIPj4un8AQ > div.ropLT > div.RRDLx > div > div
# driver.close()
# driver.quit()

