
import pandas as pd

# Sample data
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Define window size and slide
window_size = 3
slide = 1

# Perform rolling window calculations using the 'rolling' method
result = df.rolling(window_size, min_periods=1).mean()
print(result)
