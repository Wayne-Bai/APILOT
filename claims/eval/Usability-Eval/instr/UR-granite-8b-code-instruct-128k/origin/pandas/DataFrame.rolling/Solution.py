
import pandas as pd

# Create a sample dataframe
df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [2, 3, 4, 5, 6]})

# Calculate a 3-period rolling mean for column A
rolling_mean = df['A'].rolling(window=3).mean()

# Print the rolling mean
print(rolling_mean)
