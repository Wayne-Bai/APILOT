import pandas as pd

def get_group_quantile(group, quantile):
    """
    Returns group values at the given quantile.

    Parameters:
    group (Series): Input Series.
    quantile (float): Quantile value (0.0 to 1.0).

    Returns:
    float: Value at the specified quantile.
    """
    # Use the qth quantile of the given series, equivalent to numpy.percentile
    return group.quantile(quantile)

# Example usage:
data = {'A': [1, 2, 3, 4, 5]}
df = pd.DataFrame(data)

group = df['A']
quantile = 0.75  # 75th percentile

print(get_group_quantile(group, quantile))
