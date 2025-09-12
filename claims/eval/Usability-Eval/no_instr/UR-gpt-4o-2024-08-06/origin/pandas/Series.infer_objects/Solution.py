import pandas as pd

# Sample data
data = {
    'id': ['001', '002', '003'],
    'price': ['100', '200', '300'],
    'is_active': ['True', 'True', 'False'],
    'date': ['2023-01-01', '2023-02-01', '2023-03-01']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert object columns to more appropriate dtypes
df = df.convert_dtypes()

# Display the dtypes of the columns
print(df.dtypes)
