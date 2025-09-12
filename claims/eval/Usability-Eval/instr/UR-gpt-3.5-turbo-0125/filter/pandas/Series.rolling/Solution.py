
import pandas as pd

# Create a sample dataframe
data = {'value': [1, 3, 5, 7, 9]}
df = pd.DataFrame(data)

# Compute rolling window mean with window size of 2
df['rolling_mean'] = df['value'].rolling(window=2).mean()

print(df)
