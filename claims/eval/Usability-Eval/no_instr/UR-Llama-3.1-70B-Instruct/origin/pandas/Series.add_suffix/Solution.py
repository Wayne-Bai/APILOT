import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Mary', 'David'],
    'Age': [25, 31, 42]
}
df = pd.DataFrame(data)

# Suffix labels with string suffix
df = df.add_suffix('_data')

print(df)
