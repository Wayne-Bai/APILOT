import pandas as pd

# Sample DataFrame
data = {'Column1': ['apple,banana,cherry', 'dog,cat', 'red,blue,green']}
df = pd.DataFrame(data)

# Split strings around the comma separator
df['Split_Column'] = df['Column1'].str.split(',')

print(df)
