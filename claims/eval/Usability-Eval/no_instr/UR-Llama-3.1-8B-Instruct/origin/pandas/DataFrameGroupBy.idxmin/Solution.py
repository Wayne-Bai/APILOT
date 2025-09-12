import pandas as pd

def find_first_min_index(df, min_axis):
    """
    Returns the index of the first occurrence of the minimum value over the specified axis.
    
    Args:
    df (pandas DataFrame): The input DataFrame.
    min_axis (str): The axis over which to find the minimum. Can be 'columns' or 'index'.
    
    Returns:
    int: The index of the first occurrence of the minimum value.
    """
    
    # Check if min_axis is valid
    if min_axis not in ['columns', 'index']:
        raise ValueError("min_axis must be either 'columns' or 'index'")
    
    # Use the idxmin() method to get the index of the minimum value
    if min_axis == 'columns':
        result = df.stack().idxmin()
        return result
    else:
        result = df.idxmin()
        return result

# Example usage:
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)
print(find_first_min_index(df, 'columns'))
print(find_first_min_index(df, 'index'))
