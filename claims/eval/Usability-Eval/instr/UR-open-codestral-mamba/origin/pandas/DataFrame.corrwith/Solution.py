import pandas as pd

# Assuming you have a dataframe df

df = pd.DataFrame({
   'A': [1, 2, 3, 4],
   'B': [10, 20, 30, 40],
   'C': [20, 40, 60, 80],
   'D': [30, 60, 90, 120]
})

correlation_matrix = df.corr()
print(correlation_matrix)
