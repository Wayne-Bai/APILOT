# Importing necessary libraries
import pandas as pd
import numpy as np

# Generating a sample DataFrame
np.random.seed(0)
data = np.random.randn(5, 3)
df = pd.DataFrame(data, columns=list('ABC'))

# Defining a function to calculate quantile
def quantile_values(df, q, axis=0):
    """
    Return values at the given quantile over requested axis.

    Parameters:
    df (DataFrame): DataFrame to calculate quantile from
    q (float or list of floats): Quantile to calculate, in the range [0, 1]
    axis (int): {0 or 'index', 1 or 'columns'}, default 0

    Returns:
    float or Series: Values at the given quantile
    """
    if not isinstance(q, list):
        q = [q]
    
    return df.apply(lambda x: np.percentile(x, [i * 100 for i in q], axis=axis, interpolation='midpoint'), axis=axis)

# Example usage:
print("Original DataFrame:")
print(df)

print("\nQuantile values (50th percentile) over index axis:")
print(quantile_values(df, 0.5))

print("\nQuantile values (25th and 75th percentiles) over columns axis:")
print(quantile_values(df, [0.25, 0.75], axis=1))
