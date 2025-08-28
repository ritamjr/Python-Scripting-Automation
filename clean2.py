import pandas as pd

# Load scraped dataset
df = pd.read_csv("Web_Scrapping/books_categories.csv")

# 1. Remove duplicates (based on product_url to be safe)
df = df.drop_duplicates(subset=["product_url"])

# 2. Strip whitespace
df["title"] = df["title"].str.strip()
df["category"] = df["category"].str.strip()
df["product_url"] = df["product_url"].str.strip()

# 3. Optional: Normalize category text (capitalize first letter, rest lowercase)
df["category"] = df["category"].str.title()

# 4. Preview cleaned data
print(df.head())
print(f"✅ Total unique rows after cleaning: {len(df)}")

# 5. Save cleaned file
df.to_csv("Web_Scrapping/books_categories_cleaned.csv", index=False)
