import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'B': [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]}

df = pd.DataFrame(data)

# Create a new column with rolling mean
rolling_mean = df['A'].rolling(window=3).mean()

# Add the rolling mean to the DataFrame
df['Rolling Mean'] = rolling_mean

print(df)
