
import pandas as pd

# Create a sample DataFrame
data = {'A': [1, 2, 3, 4, 5],
        'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

# Perform rolling window calculations
rolling_mean = df.rolling(window=2).mean()
rolling_sum = df.rolling(window=2).sum()

print("Rolling Mean:")
print(rolling_mean)

print("\nRolling Sum:")
print(rolling_sum)
