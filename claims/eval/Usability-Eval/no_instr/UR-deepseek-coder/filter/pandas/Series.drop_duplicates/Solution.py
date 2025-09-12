import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 2, 3, 4, 4, 5]}
df = pd.DataFrame(data)

# Return Series with duplicate values removed
unique_series = df['A'].drop_duplicates()

print(unique_series)
