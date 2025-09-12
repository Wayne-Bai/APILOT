import pandas as pd

# sample data frame
df = pd.DataFrame({
   'A': [1, 2, None, 4, 5],
   'B': [6, None, 8, 9, 10],
   'C': [2, 4, 6, None, 8],
   'D': [10, None, 12, 13, 14]
})

# calculate correlation
correlation = df.corr()
print(correlation)
