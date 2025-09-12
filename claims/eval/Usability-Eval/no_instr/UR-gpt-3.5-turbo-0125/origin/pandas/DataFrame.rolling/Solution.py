
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Perform rolling window calculation (e.g., rolling sum) on column 'A' with window size 2
rolling_window_size = 2
rolled_values = df['A'].rolling(window=rolling_window_size).sum()

print(rolled_values)
