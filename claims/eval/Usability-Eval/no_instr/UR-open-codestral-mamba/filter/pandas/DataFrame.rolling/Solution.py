
import pandas as pd

# Assuming you have a DataFrame df with a column 'values'
df = pd.DataFrame({
    'values': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
})

# Calculate a simple rolling window with a window size of 3
rolling_window = df['values'].rolling(window=3)

# Calculate the mean of the rolling window
mean_rolling = rolling_window.mean()

# Calculate the standard deviation of the rolling window
std_dev_rolling = rolling_window.std()

# Print the original, mean, and standard deviation of rolling window
print("Original series:")
print(df)
print("\nMean of rolling window:")
print(mean_rolling)
print("\nStandard deviation of rolling window:")
print(std_dev_rolling)
