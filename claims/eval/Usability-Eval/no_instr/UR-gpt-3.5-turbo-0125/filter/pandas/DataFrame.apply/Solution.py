
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# Apply a function along the rows
row_sum = df.apply(lambda x: x.sum(), axis=1)
print(row_sum)

# Apply a function along the columns
col_mean = df.apply(lambda x: x.mean(), axis=0)
print(col_mean)
