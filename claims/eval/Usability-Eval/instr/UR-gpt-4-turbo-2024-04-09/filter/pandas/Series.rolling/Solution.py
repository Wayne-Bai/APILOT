import pandas as pd

# Example DataFrame
data = {
    'values': [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)

# Rolling window calculation with the window size of 3
rolling_window = df['values'].rolling(window=3)
mean_rolling = rolling_window.mean()  # Calculate mean in the rolling window
sum_rolling = rolling_window.sum()    # Calculate sum in the rolling window

# Print the results
print("Rolling Mean:\n", mean_rolling)
print("Rolling Sum:\n", sum_rolling)
