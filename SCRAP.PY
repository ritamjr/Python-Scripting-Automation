from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

all_data = []

page = 1
while True:
    url = BASE_URL.format(page)
    driver.get(url)
    time.sleep(1)
    
    books = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    if not books:  # no more pages
        break
    
    for b in books:
        title = b.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        price = b.find_element(By.CLASS_NAME, "price_color").text
        availability = b.find_element(By.CLASS_NAME, "availability").text.strip()
        rating = b.find_element(By.CSS_SELECTOR, "p.star-rating").get_attribute("class").replace("star-rating", "").strip()
        link = b.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("href")
        
        all_data.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "product_url": link
        })
    
    print(f"Scraped page {page}, total so far: {len(all_data)}")
    page += 1

driver.quit()

# Save into DataFrame
df = pd.DataFrame(all_data)
print("Total books scraped:", len(df))
print(df.head())

df.to_csv("books_all.csv", index=False)
