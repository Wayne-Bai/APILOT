import pandas as pd

# create a sample DataFrame with a column containing strings to be split
df = pd.DataFrame({'strings': ['hello,world', 'foo,bar', 'baz,qux']})

# split the strings around the comma separator/delimiter
df['splitted'] = df['strings'].str.split(',')

print(df)
