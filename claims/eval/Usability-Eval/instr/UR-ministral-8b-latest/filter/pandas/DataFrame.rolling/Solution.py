import pandas as pd

# Sample data
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Define window size
window_size = 3

# Apply rolling mean with specified window size
rolling_mean = data.rolling(window=window_size).mean()

print(rolling_mean)
