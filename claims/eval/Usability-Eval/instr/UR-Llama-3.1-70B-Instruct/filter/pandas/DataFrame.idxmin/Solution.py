import pandas as pd
import numpy as np

def find_first_min_index(data, axis):
    """
    Return index of first occurrence of minimum over requested axis.

    Parameters:
    data (Series or DataFrame): Input data.
    axis (int): Axis along which to find the minimum.

    Returns:
    int or Index: Index of the first occurrence of the minimum.
    """
    return data.argmin(axis=axis)


# Example usage:
if __name__ == "__main__":
    # Create a sample DataFrame
    np.random.seed(0)
    df = pd.DataFrame(np.random.randn(5, 5), columns=list('ABCDE'))

    # Find the index of the first occurrence of the minimum along each row (axis=0)
    row_min_index = df.apply(find_first_min_index, axis=0)
    print("Index of the first occurrence of the minimum along each row:")
    print(row_min_index)

    # Find the index of the first occurrence of the minimum along each column (axis=1)
    col_min_index = df.apply(find_first_min_index, axis=1)
    print("\nIndex of the first occurrence of the minimum along each column:")
    print(col_min_index)
