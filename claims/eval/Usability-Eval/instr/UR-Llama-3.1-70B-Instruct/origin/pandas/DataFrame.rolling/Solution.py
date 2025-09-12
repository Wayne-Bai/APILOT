# Import pandas library
import pandas as pd

# Generate sample data
data = {
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Perform rolling window calculations
window_size = 3

# Calculate rolling mean
df['rolling_mean'] = df['A'].rolling(window_size).mean()

# Calculate rolling median (50th percentile)
df['rolling_median'] = df['A'].rolling(window_size).quantile(0.5)

# Calculate rolling variance
df['rolling_variance'] = df['A'].rolling(window_size).var()

# Calculate rolling standard deviation (using np.sqrt for square root)
import numpy as np
df['rolling_std_dev'] = np.sqrt(df['A'].rolling(window_size).var())

# Print the results
print(df)
