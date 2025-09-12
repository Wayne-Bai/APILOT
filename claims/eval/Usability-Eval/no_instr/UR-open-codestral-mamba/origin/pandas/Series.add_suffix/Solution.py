import pandas as pd

# Assuming df is your DataFrame and you want to add suffix '_new' to all column labels
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df = df.add_suffix('_new')
print(df)
