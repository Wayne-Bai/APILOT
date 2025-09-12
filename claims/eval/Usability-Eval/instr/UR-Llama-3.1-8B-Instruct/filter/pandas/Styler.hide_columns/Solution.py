# Import pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "City": ["New York", "Paris", "London", "Berlin"]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Hide the column headers
df_from_records = df.apply(lambda x: x.to_list())

# Print the DataFrame with hidden column headers
print("\nDataFrame with hidden column headers:")
pd.DataFrame(df_from_records).T # which contains only values with no column names

