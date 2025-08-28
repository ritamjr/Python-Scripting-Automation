import psycopg2
import pandas as pd

# Load cleaned CSV
df = pd.read_csv("books_cleaned.csv")

# Database connection settings
conn = psycopg2.connect(
    dbname="scrape_book",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price NUMERIC(6,2) NOT NULL,
    availability INT NOT NULL,
    rating SMALLINT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    product_url TEXT NOT NULL
);
"""
cur.execute(create_table_query)
conn.commit()

# Insert data row by row
insert_query = """
INSERT INTO books (title, price, availability, rating, product_url)
VALUES (%s, %s, %s, %s, %s);
"""

for _, row in df.iterrows():
    cur.execute(insert_query, tuple(row))

# Commit and close
conn.commit()
cur.close()
conn.close()

print("✅ Data uploaded successfully into scrape_book.books")
