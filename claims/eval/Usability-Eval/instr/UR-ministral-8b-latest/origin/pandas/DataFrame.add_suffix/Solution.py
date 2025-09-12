import pandas as pd

# Sample DataFrame
data = {
    'name': ['one', 'two', 'three', 'four'],
    'value': [10, 20, 30, 40]
}
df = pd.DataFrame(data)

# Suffix labels with string suffix
df['name'] = df['name'].str.cat('suffix')

print(df)
