# Import pandas library
import pandas as pd

# Sample data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Tokyo', 'Sydney']
}

# Create DataFrame
df = pd.DataFrame(data)

# Display entire DataFrame with index and column headers
print("Entire DataFrame:")
print(df)

# Hide entire index from display
print("\nHide entire index from display:")
print(df.to_string(index=False))

# Hide entire column headers from display
print("\nHide entire column headers from display:")
print(df.columns)
print(df.to_string(header=False, index=False))

# Hide specific rows from display
print("\nHide specific rows from display:")
print(df.iloc[1:, :])

# Hide specific columns from display
print("\nHide specific columns from display:")
print(df[['Name', 'Age']])

# Hide specific rows and columns from display
print("\nHide specific rows and columns from display:")
print(df.loc[1:, ['Name', 'Age']])
