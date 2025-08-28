import pandas as pd

# Load the scraped dataset
df = pd.read_csv("books_all.csv")

# 1. Clean price (remove £ and convert to float)
df["price"] = df["price"].str.replace("£", "", regex=False).astype(float)

# 2. Clean availability (extract number if present, else 1 for In stock, 0 otherwise)
df["availability"] = df["availability"].str.extract(r"(\d+)")  # extract digits
df["availability"] = df["availability"].fillna("1")  # assume "In stock" means 1
df["availability"] = df["availability"].astype(int)

# 3. Convert rating words to numbers
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["rating"] = df["rating"].map(rating_map)

# 4. Drop unnecessary columns (if description exists)
if "description" in df.columns:
    df = df.drop(columns=["description"])

# 5. Final cleaned dataframe preview
print(df.dtypes)
print(df.head())

# 6. Save cleaned version for database upload
df.to_csv("books_cleaned.csv", index=False)
