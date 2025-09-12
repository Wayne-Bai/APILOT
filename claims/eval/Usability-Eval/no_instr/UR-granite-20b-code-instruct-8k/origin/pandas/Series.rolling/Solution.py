import pandas as pd

# create a dataframe
data = {'A': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

# create a rolling window of size 2
rolling_window = df.rolling(2)

# calculate the sum of values in the rolling window
rolling_sum = rolling_window.sum()

# print the result
print(rolling_sum)
