# Import pandas library
import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Hide the entire index and column headers
print("\nHide the entire index and column headers:")
print(df.to_string(index=False, header=False))

# Hide specific rows
print("\nHide specific rows (e.g., 1st and 3rd row):")
print(df.to_string(index=False, header=True).split('\n')[[0, 2, 3]])

# Hide specific columns
print("\nHide specific columns (e.g., 'Age' column):")
print(df[['Name', 'City']].to_string(index=False))

# Hide specific rows and columns
print("\nHide specific rows and columns (e.g., 1st row and 'Age' column):")
print(df[['Name', 'City']].to_string(index=False).split('\n')[1:])
