import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'Score': [90, 85, 88]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Hide the column headers
print("\nDataFrame with hidden column headers:")
print(df.to_string(index=False, header=False))

# Hide specific column headers
print("\nDataFrame with hidden 'Score' column header:")
print(df.rename(columns={'Score': ''}).to_string(index=False))

# Alternatively, you can use the following approach
print("\nDataFrame with hidden 'Score' column header:")
print(df.to_string(index=False).replace('Score', ''))
