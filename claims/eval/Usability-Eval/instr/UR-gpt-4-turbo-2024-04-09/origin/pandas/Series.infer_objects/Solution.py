import pandas as pd

# Sample data creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': ['30', '25', '35'],
    'Income': ['50000', '48000', '55000']
}

df = pd.DataFrame(data)

# Convert object columns to more specific types automatically
df = df.convert_dtypes()

print(df.dtypes)
