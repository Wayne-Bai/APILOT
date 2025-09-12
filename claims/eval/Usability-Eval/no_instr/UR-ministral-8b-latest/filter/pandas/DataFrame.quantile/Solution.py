import pandas as pd

def calculate_quantile(values, quantile, axis):
    """
    Calculate the quantile of the values along the given axis.

    Parameters:
    - values: the input data Emirates
    - quantile: the requested quantile to be returned
    - axis: the axis along which to calculate the quantile

    Returns:
    - quantile_value: the value at the requested quantile
    """

    series = pd.Series(values)
    quantile_value = series.quantile(quantile, axis=axis)
    return quantile_value

# Example usage:
# data = [1, 2, 3, 4, 5]
# quantile_value = calculate_quantile(data, 0.5, 0)
# print(quantile_value)  # This will print 3.0
