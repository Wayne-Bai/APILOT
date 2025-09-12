import pandas as pd

# Let's assume df is our DataFrame and 'A' is the column for which we need to find the quantile.
percentile_value = 0.5  # This is the quantile we want (i.e., 50th percentile)

# Calculate quantile
quantile_value = df['A'].quantile(percentile_value)
