import pandas as pd

# Example DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'income': ['50000', '60000', '70000']
}
df = pd.DataFrame(data)

# Convert object types to more specific data types automatically
df = df.convert_dtypes()

print(df.dtypes)
