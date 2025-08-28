import psycopg2
import random
import datetime
import faker


fake = faker.Faker()

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="retail_db",
    user="postgres",
    password="1234"
)
cur = conn.cursor()


categories = {
    "Electronics": (500, 50000),
    "Clothing": (200, 5000),
    "Home Appliances": (1000, 30000),
    "Books": (100, 2000),
    "Toys": (50, 5000),
    "Groceries": (20, 2000)
}

def generate_transaction(transaction_id):
    customer_id = random.randint(1000, 2000)
    gender = random.choice(["Male", "Female"])
    age = random.randint(18, 65)
    category = random.choice(list(categories.keys()))
    quantity = random.randint(1, 5)
    price = random.randint(categories[category][0], categories[category][1])
    total = quantity * price
    date = fake.date_between(start_date="-30d", end_date="today")

    return (
        transaction_id, date, customer_id, gender, age,
        category, quantity, price, total
    )

def insert_transactions(n=50):
    for i in range(n):
        txn = generate_transaction(random.randint(10000, 99999))
        cur.execute("""
    INSERT INTO transactions 
    (transaction_id, date, customer_id, gender, age, 
     product_category, quantity, price_per_unit, total_amount)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
""", txn)

    conn.commit()
    print(f"✅ {n} new transactions inserted into PostgreSQL")

if __name__ == "__main__":
    insert_transactions(50)  

    cur.close()
    conn.close()
    
    
#     1) Run script daily/hourly (recommended):
#    - Windows: Use Task Scheduler → Schedule `python data_gen.py`
#    - Linux/Mac: Use `cron` → e.g., run every hour: 0 * * * * python3 /path/data_gen.py

