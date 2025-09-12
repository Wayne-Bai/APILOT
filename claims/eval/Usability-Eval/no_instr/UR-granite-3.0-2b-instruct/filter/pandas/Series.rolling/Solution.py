import pandas as pd

# Assuming df is your DataFrame and window_size is the size of the rolling window
df = pd.DataFrame({
    'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

window_size = 3

# Create a rolling window function
def rolling_window(data, window_size):
    return data.rolling(window_size).mean()

# Apply the rolling window function to the DataFrame
df['rolling_mean'] = rolling_window(df['values'], window_size)

print(df)
