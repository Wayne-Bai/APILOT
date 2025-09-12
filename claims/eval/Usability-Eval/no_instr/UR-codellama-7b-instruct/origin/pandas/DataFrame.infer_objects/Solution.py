
import pandas as pd

# Load the data into a pandas dataframe
df = pd.read_csv("data.csv")

# Convert all object columns to categories
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype("category")

# Drop any unnecessary columns and save the result to a new CSV file
df.drop(["unnecessary_column1", "unnecessary_column2"], axis=1, inplace=True)
df.to_csv("data_processed.csv", index=False)
