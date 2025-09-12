import pandas as pd

# Sample DataFrame
data = {
    'names': ['John,Doe,Smith', 'Jane,Doe,Johnson', 'Jim,Beam,Turner'],
    'ages': [25, 30, 35]
}
df = pd.DataFrame(data)

# Split strings around given separator/delimiter
df['names_split'] = df['names'].str.split(',')

print(df)
