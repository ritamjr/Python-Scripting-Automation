import requests
import pandas as pd
import os

BASE_URL = "https://api.spaceflightnewsapi.net/v4/articles"
PAGE_SIZE = 100   # max allowed
MAX_RECORDS = 1000   # adjust as needed

all_articles = []
page = 1

while len(all_articles) < MAX_RECORDS:
    url = f"{BASE_URL}?page={page}&page_size={PAGE_SIZE}"
    response = requests.get(url)
    response.raise_for_status()
    
    data = response.json()
    results = data.get("results", [])
    
    if not results:
        break  # stop if no more data
    
    all_articles.extend(results)
    print(f"Fetched page {page}, total records so far: {len(all_articles)}")
    
    # Stop if we already have enough
    if len(all_articles) >= MAX_RECORDS:
        break
    
    page += 1

# Convert to DataFrame
df = pd.DataFrame(all_articles)

# Rename columns to meaningful names
mapping = {
    "id": "article_id",
    "title": "headline",
    "url": "article_url",
    "image_url": "image_url",
    "news_site": "source",
    "summary": "summary_text",
    "published_at": "published_date"
}
df = df[list(mapping.keys())].rename(columns=mapping)

# Clean and convert types
df["article_id"] = df["article_id"].astype(int)
df["headline"] = df["headline"].astype(str).str.strip()
df["article_url"] = df["article_url"].astype(str)
df["image_url"] = df["image_url"].astype(str)
df["source"] = df["source"].astype(str)
df["summary_text"] = df["summary_text"].fillna("No summary").astype(str)
df["published_date"] = pd.to_datetime(df["published_date"], errors="coerce").dt.tz_localize(None)

# Save to CSV
output_dir = r"D:\Automation Project Sub Folder"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "spaceflight_news.csv")
df.to_csv(output_file, index=False, encoding="utf-8")

print(f"✅ Saved {len(df)} cleaned articles to:\n{output_file}")
