import pandas as pd

# Assuming you have a DataFrame df
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 9],
    'C': [9, 8, 7, 6, 5]
})

def calculate_quantile(df, quantile, axis):
    """
    This function calculates the value at a given quantile over a specified axis.

    Parameters:
    df (DataFrame): The DataFrame from which to calculate the quantile.
    quantile (float): The quantile to be calculated (between 0 and 1).
    axis (int): The axis over which to calculate the quantile (0 for index-wise, 1 for column-wise).

    Returns:
    series: A Series with the calculated values of the quantile.
    """
    if axis not in [0, 1]:
        raise ValueError("Axis must be either 0 or 1.")

    return df.quantile(quantile, axis=axis)

# Calculate the value at the 0.5 quantile over the columns
result = calculate_quantile(df, 0.5, 1)
print(result)
