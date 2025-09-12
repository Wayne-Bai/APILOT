# Import pandas library
import pandas as pd

# Create a DataFrame with missing values
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', None],
    'Age': [28, 24, None, 35, 32],
    'City': ['New York', None, 'London', 'Paris', 'Berlin']
}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Remove rows with missing values
df_cleaned = df.dropna()

# Display the DataFrame after removing missing values
print("\nDataFrame after removing missing values:")
print(df_cleaned)

# Alternatively, remove columns with missing values
df_cleaned_cols = df.dropna(axis=1)

# Display the DataFrame after removing columns with missing values
print("\nDataFrame after removing columns with missing values:")
print(df_cleaned_cols)
