import pandas as pd

# Define the dataframe
df = pd.DataFrame({
   'A': [7, 2, 9, 4, 5],
   'B': [1, 6, 3, 8, 5],
   'C': [4, 3, 7, 2, 9],
})

# Find the index of the first occurrence of the maximum value over a column
max_index = df['A'].idxmax()

print("The index of the first occurrence of the maximum value in column 'A' is:", max_index)
