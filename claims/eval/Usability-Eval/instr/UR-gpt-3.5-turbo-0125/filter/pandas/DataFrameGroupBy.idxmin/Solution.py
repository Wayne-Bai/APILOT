
import pandas as pd

# Create a sample DataFrame
data = {'A': [3, 2, 5, 1, 4],
        'B': [8, 5, 3, 9, 2]}
df = pd.DataFrame(data)

# Find the index of the first occurrence of the minimum value in column 'A'
min_index_A = df['A'].idxmin()

# Find the index of the first occurrence of the minimum value in column 'B'
min_index_B = df['B'].idxmin()

print("Index of first occurrence of minimum value in column 'A':", min_index_A)
print("Index of first occurrence of minimum value in column 'B':", min_index_B)
