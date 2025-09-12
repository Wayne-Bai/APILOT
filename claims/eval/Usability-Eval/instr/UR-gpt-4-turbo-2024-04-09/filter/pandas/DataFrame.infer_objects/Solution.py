import pandas as pd

# Sample data loading
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': ['25', '30', '35'], 'income': ['50000', '60000', '70000']}
df = pd.DataFrame(data)

# Convert columns to more appropriate dtypes
df = df.convert_dtypes()

print(df.dtypes)
