import pandas as pd

# Create a simple DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3, 4, 5],
   'B': [100, 200, 300, 400, 500]
})

# Calculate the sum of column 'A'
sum_A = df['A'].sum()
print(f"Sum of column A: {sum_A}")

# Calculate the mean of column 'B'
mean_B = df['B'].mean()
print(f"Mean of column B: {mean_B}")

# Calculate the maximum value in column 'A'
max_A = df['A'].max()
print(f"Maximum value in column A: {max_A}")

# Calculate the minimum value in column 'B'
min_B = df['B'].min()
print(f"Minimum value in column B: {min_B}")
