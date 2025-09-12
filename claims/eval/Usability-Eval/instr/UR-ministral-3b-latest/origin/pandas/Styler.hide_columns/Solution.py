import pandas as pd

# Example DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter'],
    'Age': [28, 24, 35],
    'Key': ['key1', 'key2', 'key3']
}
df = pd.DataFrame(data)

# Display DataFrame without column headers
df = pd.DataFrame(df.values, columns=[None] * len(df.columns))

print(df)
