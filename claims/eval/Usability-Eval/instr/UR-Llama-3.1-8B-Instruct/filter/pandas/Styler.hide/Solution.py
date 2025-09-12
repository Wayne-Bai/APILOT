# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["John", "Anna", "Peter", "Linda"],
    "Age": [28, 24, 35, 32],
    "Country": ["USA", "UK", "Australia", "Germany"]
}
df = pd.DataFrame(data)

# Print the original DataFrame with index and column headers
print("Original DataFrame:")
print(df)

# Hide entire index
print("\nDataFrame with index hidden:")
print(df.to_string(index=False))

# Hide specific column
print("\nDataFrame with 'Country' column hidden:")
print(df.drop(columns=['Country']).to_string(index=False))

# Hide specific rows
print("\nDataFrame with rows where Age is greater than 30 hidden:")
print(df[pd.api.eval("Age <= 30")].to_string(index=False))

# Hide index and column headers
print("\nDataFrame with index and column headers hidden:")
print(df.to_string(index=False, header=False))
