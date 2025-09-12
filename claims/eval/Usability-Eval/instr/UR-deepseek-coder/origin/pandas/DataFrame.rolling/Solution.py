import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

df = pd.DataFrame(data)

# Rolling window calculations
window_size = 3

# Rolling mean
df['A_rolling_mean'] = df['A'].rolling(window=window_size).mean()

# Rolling sum
df['A_rolling_sum'] = df['A'].rolling(window=window_size).sum()

# Rolling max
df['A_rolling_max'] = df['A'].rolling(window=window_size).max()

# Rolling min
df['A_rolling_min'] = df['A'].rolling(window=window_size).min()

print(df)
