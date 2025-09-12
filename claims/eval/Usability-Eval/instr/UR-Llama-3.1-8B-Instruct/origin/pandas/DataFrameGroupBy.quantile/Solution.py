import pandas as pd
import numpy as np

def get_quantile(group, quantile, interpolation='linear'):
    """
    Return group values at the given quantile.

    Parameters:
    group (Series or DataFrame): Input series or dataframe.
    quantile (float): Quantile to compute.
    interpolation (str, optional): Interpolation method passed to np.percentile. Defaults to 'linear'.

    Returns:
    float or Series: Value(s) at the given quantile.
    """
    return np.percentile(group, quantile * 100, interpolation=interpolation)


# Example usage:
data = {'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

group_A = df['A']
group_B = df['B']

print(get_quantile(group_A, 0.5))     # Median of group A
print(get_quantile(group_B, 0.75))    # 75th percentile of group B
