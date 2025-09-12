
import pandas as pd

# Create a sample dataframe
data = {'value': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Perform rolling window calculations
window_size = 2
df['rolling_mean'] = df['value'].rolling(window=window_size).mean()
df['rolling_sum'] = df['value'].rolling(window=window_size).sum()

print(df)
