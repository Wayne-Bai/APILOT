import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5, 6],
    'B': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Rolling window calculation
# Example: Calculate the rolling mean with a window size of 3
df['A_rolling_mean'] = df['A'].rolling(window=3).mean()
df['B_rolling_sum'] = df['B'].rolling(window=3).sum()

print(df)
