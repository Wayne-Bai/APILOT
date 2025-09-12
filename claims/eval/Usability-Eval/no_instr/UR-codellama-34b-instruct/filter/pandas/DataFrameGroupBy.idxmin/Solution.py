import pandas as pd

# create sample data
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# find index of minimum value in column A
min_index = df['A'].idxmin()
print(min_index)  # prints 0
