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
df['rolling_mean_A'] = df['A'].rolling(window=window_size).mean()
df['rolling_mean_B'] = df['B'].rolling(window=window_size).mean()

# Rolling sum
df['rolling_sum_A'] = df['A'].rolling(window=window_size).sum()
df['rolling_sum_B'] = df['B'].rolling(window=window_size).sum()

# Rolling max
df['rolling_max_A'] = df['A'].rolling(window=window_size).max()
df['rolling_max_B'] = df['B'].rolling(window=window_size).max()

# Rolling min
df['rolling_min_A'] = df['A'].rolling(window=window_size).min()
df['rolling_min_B'] = df['B'].rolling(window=window_size).min()

print(df)
