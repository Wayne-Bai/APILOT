
import pandas as pd

# sample data
data = {'A': [1, 1, 2, 2, 3, 3], 'B': [4, 5, 6, 7, 8, 9]}
df = pd.DataFrame(data)

# compute min value of group
min_vals = df.groupby('A')['B'].min()
print(min_vals)
