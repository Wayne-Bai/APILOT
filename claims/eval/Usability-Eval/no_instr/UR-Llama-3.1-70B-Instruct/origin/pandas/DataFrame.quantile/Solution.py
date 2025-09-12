# Import the pandas library
import pandas as pd
import numpy as np

# Create a DataFrame
data = np.random.normal(0, 1, (5, 5))
df = pd.DataFrame(data, columns=list('ABCDE'))

# Set quantile value(s)
quantile = 0.75  # 75th percentile

# Calculate the values at the given quantile
quantiles_df = df.quantile(quantile, axis=0)

# Print the results
print("Original DataFrame:")
print(df)
print("\nValues at {} quantile:".format(quantile))
print(quantiles_df)

# Calculate quantiles along rows (axis=1)
print("\nValues at {} quantile (along rows):".format(quantile))
print(df.quantile(quantile, axis=1))

# Calculate multiple quantiles
quantiles = [0.25, 0.5, 0.75]
print("\nValues at {} quantiles:".format(quantiles))
print(df.quantile(quantiles, axis=0))
