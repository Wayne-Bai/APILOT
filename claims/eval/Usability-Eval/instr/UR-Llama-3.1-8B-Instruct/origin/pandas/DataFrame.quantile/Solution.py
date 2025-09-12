import pandas as pd

def return_quantile(df, quantile, axis):
    """
    Return values at the given quantile over requested axis.

    Parameters:
    df (pd.DataFrame): Input DataFrame.
    quantile (float): Quantile value between 0 and 1.
    axis (int): Axis to calculate quantile along. 
                0 for rows, 1 for columns.

    Returns:
    float or np.array: Values at the given quantile over the requested axis.
    """
    
    # Check if axis is valid
    if axis not in [0, 1]:
        raise ValueError("Axis must be 0 for rows or 1 for columns.")
    
    # Calculate quantile along the given axis
    if axis == 0:
        result = df.quantile(quantile, axis=axis)
    else:
        result = df.quantile(quantile, axis=axis)
    
    return result

# Example usage
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [2, 4, 6, 8, 10]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

quantile_value = 0.5
axis_value = 0  # Calculate for rows

result = return_quantile(df, quantile_value, axis_value)
print("\nValues at", quantile_value, "quantile along axis", axis_value, ":")
print(result)
