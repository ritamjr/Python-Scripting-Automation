import pandas as pd
from sqlalchemy import create_engine

# Loading CSV in our dataframe
df = pd.read_csv("C:\\Users\\Ritam\\OneDrive\\Desktop\\Projects\\Automation Project\\transactions\\transactions.csv")

# Creating PostgreSQL connection with our py file
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/retail_db")

# Loading the data into PostgreSQL to the respective database
df.to_sql("transactions", engine, if_exists="replace", index=False)

print("✅ 1000 transactions imported into PostgreSQL successfully!")
