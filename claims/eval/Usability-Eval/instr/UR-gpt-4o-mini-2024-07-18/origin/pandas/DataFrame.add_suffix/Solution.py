import pandas as pd

# Sample DataFrame
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
df = pd.DataFrame(data)

# Adding a suffix to column labels
df.columns = [col + '_suffix' for col in df.columns]

print(df)
