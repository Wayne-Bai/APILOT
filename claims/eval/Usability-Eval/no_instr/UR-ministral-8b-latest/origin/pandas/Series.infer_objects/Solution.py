import pandas as pd

# Sample data
data = {
    'A': ['10', '20', '30', '40'],
    'B': ['50.5', '60.6', '70.7', '80.8'],
    'C': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Print original data types
print("Original DataTypes:")
print(df.dtypes)

# Inferred data types
df['A'] = pd.to_numeric(df['A'])
df['B'] = pd.to_numeric(df['B']).astype('float')
df['C'] = pd.to_datetime(df['C'])

# Print inferred data types
print("\nInferred DataTypes:")
print(df.dtypes)
