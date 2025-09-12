
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# calculate the rolling sum of column A with window size 3
rolling_sum = df['A'].rolling(window=3).sum()
