import pandas as pd

# Assuming you have a DataFrame named df with columns 'A' and 'B'
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1]
})

# Grouping by a specific column and computing the sum for the 'B' column
grouped_df = df.groupby('A')['B'].sum()  # You can replace 'B' with the column you want to sum
print(grouped_df)
