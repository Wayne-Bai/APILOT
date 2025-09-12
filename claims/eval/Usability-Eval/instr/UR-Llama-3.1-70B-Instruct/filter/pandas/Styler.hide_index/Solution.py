# Importing the pandas library
import pandas as pd

# Data for the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
    'Age': [25, 32, 41, 35],
    'Country': ['USA', 'UK', 'France', 'Germany']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Set 'Name' as the index
df.set_index('Name', inplace=True)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Hide the index
print("\nDataFrame with hidden index:")
print(df.to_string(index=False))

# Unhide the index
print("\nDataFrame with unhidden index:")
print(df)

# Print the DataFrame in a style that hides the index, and also print the DataFrame as is for comparison
print("\nDataFrame with specified keys hidden from index:")
for key in list(df.index):
    if key!= 'Bob':
        print(key, ":", df.loc[key].to_list())
print("\nDataFrame as is:")
print(df)

# Hide Specific keys in the index
specific_keys = ['Bob', 'Charlie']
for key in list(df.index):
    if key not in specific_keys:
        print(key, ":", df.loc[key].to_list())
