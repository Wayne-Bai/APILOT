import pandas as pd

# Let's consider we have this pandas DataFrame df:
df = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6],
   'C': [7, 8, 9]
})

# To get the sum of all values in column 'A' we can do the following:
sum_A = df['A'].sum()

print(sum_A)
