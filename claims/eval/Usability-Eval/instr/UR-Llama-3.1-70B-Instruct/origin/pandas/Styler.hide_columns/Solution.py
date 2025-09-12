# Importing pandas library
import pandas as pd

# Sample data for DataFrame
data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Create DataFrame
df = pd.DataFrame(data)

# Print original DataFrame
print("Original DataFrame:")
print(df)

# Hide column headers
df.columns = [""] * len(df.columns)

# Print DataFrame with hidden column headers
print("\nDataFrame with hidden column headers:")
print(df)

# Hide specific column headers
df.columns = ["Name" if col == "Name" else "" for col in df.columns]

# Print DataFrame with specific hidden column headers
print("\nDataFrame with specific hidden column headers:")
print(df)
