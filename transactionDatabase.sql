CREATE TABLE transactions (
    TransactionID VARCHAR(20) PRIMARY KEY,
    Date DATE,
    CustomerID VARCHAR(20),
    Gender VARCHAR(10),
    Age INT,
    ProductCategory VARCHAR(50),
    Quantity INT,
    PricePerUnit DECIMAL(10,2),
    TotalAmount DECIMAL(12,2)
);


SELECT SUM("Total Amount") FROM transactions;

SELECT "Product Category", SUM("Total Amount") as Total_Amount
FROM transactions
GROUP BY "Product Category"
ORDER BY 2 DESC;


SELECT "Customer ID", SUM("Total Amount") AS total_spent
FROM transactions
GROUP BY "Customer ID"
ORDER BY total_spent DESC
LIMIT 5;

SELECT * FROM transactions


SELECT column_name 
FROM information_schema.columns 
WHERE table_name = 'transactions';


ALTER TABLE transactions RENAME COLUMN "Transaction ID" TO transaction_id;
ALTER TABLE transactions RENAME COLUMN "Date" TO date;
ALTER TABLE transactions RENAME COLUMN "Customer ID" TO customer_id;
ALTER TABLE transactions RENAME COLUMN "Gender" TO gender;
ALTER TABLE transactions RENAME COLUMN "Age" TO age;
ALTER TABLE transactions RENAME COLUMN "Product Category" TO product_category;
ALTER TABLE transactions RENAME COLUMN "Quantity" TO quantity;
ALTER TABLE transactions RENAME COLUMN "Price per Unit" TO price_per_unit;
ALTER TABLE transactions RENAME COLUMN "Total Amount" TO total_amount;

SELECT * FROM transactions LIMIT 10;
SELECT COUNT(*) FROM transactions;


