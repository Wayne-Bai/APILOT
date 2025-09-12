
import pandas as pd

# Define the mapping or function to use for the mapping
mapping = {
    "value1": 10,
    "value2": 20,
    "value3": 30
}

def map_values(df):
    # Create a new column in the DataFrame with the mapped values
    df["mapped"] = df["original"].map(mapping)
    return df

# Load the data into a Pandas DataFrame
data = pd.read_csv("data.csv")

# Apply the mapping to the DataFrame
result = map_values(data)

# Print the resulting DataFrame
print(result)
