import pandas as pd

data = {'Column': [1, 2, 3, 4, 3, 2, 1]}
df = pd.DataFrame(data)

unique_series = df['Column'].drop_duplicates()

print(unique_series)
