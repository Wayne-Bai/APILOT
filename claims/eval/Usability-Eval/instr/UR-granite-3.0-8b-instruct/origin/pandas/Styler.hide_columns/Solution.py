import pandas as pd

# Assuming df is your DataFrame and you want to hide columns 'A' and 'B'
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

# Hide columns 'A' and 'B'
df = df.loc[:, ~df.columns.str.contains('A|B')]

print(df)
