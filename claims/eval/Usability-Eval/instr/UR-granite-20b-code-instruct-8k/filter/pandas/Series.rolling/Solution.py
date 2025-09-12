import pandas as pd

# Create a dataframe
data = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
df = pd.DataFrame(data)

# Calculate rolling mean
rolling_mean = df['A'].rolling(window=3).mean()

# Print the rolling mean
print(rolling_mean)
