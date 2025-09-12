import pandas as pd
import numpy as np

# Example DataFrame
data = {
    'group': ['A', 'A', 'A', 'B', 'B', 'B'],
    'value': [10, 20, 30, 40, 50, 60]
}

df = pd.DataFrame(data)

# Determine which quantile you want to calculate
quantile_value = 0.5  # For median, use 0.5, for 25th percentile use 0.25, etc.

# Function to apply to each group to get the desired quantile
def quantile_calculation(x):
    return np.percentile(x, quantile_value * 100)

# Group by the 'group' column and apply the quantile calculation
result = df.groupby('group')['value'].apply(quantile_calculation).reset_index()

result.columns = ['group', 'quantile_value']

print(result)
