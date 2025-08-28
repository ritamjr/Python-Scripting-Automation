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
    if not books:
        break

    for b in books:
        title = b.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
        link = b.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("href")

        # go inside detail page
        driver.get(link)
        time.sleep(0.5)

        breadcrumb = driver.find_elements(By.CSS_SELECTOR, "ul.breadcrumb li a")
        # index 2 is the real category (like Travel, Mystery, etc.)
        category = breadcrumb[2].text if len(breadcrumb) > 2 else "Unknown"

        driver.back()
        time.sleep(0.5)

        all_data.append({
            "title": title,
            "category": category,
            "product_url": link   # 🔹 Added so we can map safely later
        })

    print(f"Scraped page {page}, total so far: {len(all_data)}")
    page += 1

driver.quit()

df = pd.DataFrame(all_data)
print("Total books scraped:", len(df))
print(df.head())

df.to_csv("Web_Scrapping\\books_categories.csv", index=False)
