
import pandas as pd

# Sample Series
data = {'A': 1, 'B': 2, 'C': 3}
series = pd.Series(data)

# Prefix labels in Series
series.index = "prefix_" + series.index.astype(str)

# Sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# Prefix labels in DataFrame
df.columns = "prefix_" + df.columns.astype(str)

print(series)
print(df)
