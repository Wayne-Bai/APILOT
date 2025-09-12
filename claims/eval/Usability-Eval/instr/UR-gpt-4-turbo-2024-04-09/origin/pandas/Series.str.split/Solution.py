import pandas as pd

# Sample data in a DataFrame
data = {
    'column': ['apple,banana', 'orange,kiwi', 'strawberry,blueberry']
}
df = pd.DataFrame(data)

# Splitting the strings in the 'column' around the comma separator
df['split_column'] = df['column'].str.split(',')

print(df)
