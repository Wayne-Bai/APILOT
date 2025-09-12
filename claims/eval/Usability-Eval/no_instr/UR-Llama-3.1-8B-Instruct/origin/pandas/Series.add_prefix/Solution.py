# Importing pandas library
import pandas as pd

# Creating a dictionary for data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Tokyo', 'Sydney']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Printing the original DataFrame
print("Original DataFrame:")
print(df)

# Prefixing the column labels with 'Country - '
df.columns = 'Country -'+ df.columns

# Printing the updated DataFrame
print("\nUpdated DataFrame with prefixed column labels:")
print(df)
