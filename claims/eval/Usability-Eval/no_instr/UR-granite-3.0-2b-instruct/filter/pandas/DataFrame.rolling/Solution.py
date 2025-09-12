import pandas as pd

# Assuming df is your DataFrame and window_size is the size of the rolling window
window_size = 3

# Create a rolling window function
def rolling_window(data, window_size):
    return [data[i:i+window_size] for i in range(len(data) - window_size + 1)]

# Apply the rolling window function to your DataFrame
rolling_windows = rolling_window(df, window_size)

# Now you can perform calculations on each rolling window
for i, window in enumerate(rolling_windows):
    # For example, let's calculate the mean of each window
    mean_value = window.mean()
    print(f"Mean value of window {i+1}: {mean_value}")
