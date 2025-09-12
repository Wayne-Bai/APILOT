import pandas as pd

# Sample DataFrame with object dtypes
data = {
    'integers': ['1', '2', '3', '4'],
    'floats': ['1.1', '2.2', '3.3', '4.4'],
    'dates': ['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01'],
    'strings': ['apple', 'banana', 'cherry', 'date']
}

df = pd.DataFrame(data)

# Attempt to infer better dtypes for object columns
df = df.convert_dtypes()

# Individually converting columns if needed
df['dates'] = pd.to_datetime(df['dates'])
df['integers'] = pd.to_numeric(df['integers'])
df['floats'] = pd.to_numeric(df['floats'])

# Display the resulting DataFrame with inferred dtypes
print(df.dtypes)
print(df)
