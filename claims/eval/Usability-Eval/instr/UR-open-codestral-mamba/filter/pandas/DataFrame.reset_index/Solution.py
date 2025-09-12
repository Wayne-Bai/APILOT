import pandas as pd

# Assuming 'df' is your DataFrame
df = pd.DataFrame({'A': ['foo', 'bar', 'baz'], 'B': ['one', 'one', 'two']})

df = df.reset_index(drop=True)

print(df)
