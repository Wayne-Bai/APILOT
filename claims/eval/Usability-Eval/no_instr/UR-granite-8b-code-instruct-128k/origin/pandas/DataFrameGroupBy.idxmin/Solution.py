import pandas as pd

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3, 2, 1],
    'B': [4, 5, 6, 5, 4],
    'C': [7, 8, 9, 8, 7]
})

# Find the index of the first occurrence of the minimum value in column 'A'
min_index_A = df['A'].idxmin()

# Find the index of the first occurrence of the minimum value in column 'B'
min_index_B = df['B'].idxmin()

# Find the index of the first occurrence of the minimum value in column 'C'
min_index_C = df['C'].idxmin()

print(f'Index of first occurrence of minimum in column A: {min_index_A}')
print(f'Index of first occurrence of minimum in column B: {min_index_B}')
print(f'Index of first occurrence of minimum in column C: {min_index_C}')
