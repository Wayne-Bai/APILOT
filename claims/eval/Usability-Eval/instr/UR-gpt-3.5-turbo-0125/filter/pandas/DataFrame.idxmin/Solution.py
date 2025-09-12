
import pandas as pd

# Create a sample dataframe
data = {'A': [10, 20, 15, 25],
        'B': [5, 10, 8, 12]}
df = pd.DataFrame(data)

# Find the index of the first occurrence of minimum value in column 'A'
min_index_A = df['A'].idxmin()

# Find the index of the first occurrence of minimum value in column 'B'
min_index_B = df['B'].idxmin()

print('Index of first occurrence of minimum value in column A:', min_index_A)
print('Index of first occurrence of minimum value in column B:', min_index_B)
