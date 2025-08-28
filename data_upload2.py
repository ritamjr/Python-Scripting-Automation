import psycopg2
import pandas as pd

# Load cleaned categories CSV
df = pd.read_csv("Web_Scrapping/books_categories_cleaned.csv")

# Database connection
conn = psycopg2.connect(
    dbname="scrape_book",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# 1. Create book_categories table
create_table_query = """
CREATE TABLE IF NOT EXISTS book_categories (
    id SERIAL PRIMARY KEY,
    book_id INT NOT NULL,
    category VARCHAR(100) NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE
);
"""
cur.execute(create_table_query)
conn.commit()

# 2. Get book_id mapping from books table using product_url
cur.execute("SELECT id, product_url FROM books;")
book_map = {url.strip(): book_id for book_id, url in cur.fetchall()}

# 3. Insert categories
insert_query = """
INSERT INTO book_categories (book_id, category) VALUES (%s, %s)
ON CONFLICT DO NOTHING;
"""

inserted = 0
for _, row in df.iterrows():
    product_url = row["product_url"].strip()
    category = row["category"]
    book_id = book_map.get(product_url)

    if book_id:  # Only insert if book exists in books table
        cur.execute(insert_query, (book_id, category))
        inserted += 1

conn.commit()
cur.close()
conn.close()

print(f"✅ Successfully uploaded {inserted} categories into scrape_book.book_categories")
