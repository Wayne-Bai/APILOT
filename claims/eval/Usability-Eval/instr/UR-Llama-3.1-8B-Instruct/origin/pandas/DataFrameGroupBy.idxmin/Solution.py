import pandas as pd

def get_first_occurrence_of_min(df, axis=0):
    """
    Returns the index of the first occurrence of the minimum value over the requested axis.
    NA/null values are excluded.

    Parameters:
    df (DataFrame): The DataFrame to search in.
    axis (int, optional): The axis to search over. Defaults to 0 (rows).

    Returns:
    int: The index of the first occurrence of the minimum value.
    """
    # Replace NA/null values with a very large number
    df = df.fillna(1e20)

    # Find the minimum value over the requested axis
    min_val = df.min(axis=axis)

    # Filter the original DataFrame to get the first occurrence of the minimum value
    min_row = df.eq(min_val, axis=axis)

    # Find the index of the first True value in the filtered DataFrame
    index = min_row.idxmax()

    return index

# Example usage
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40],
    'C': [2, 5, 7, None]
})

print(get_first_occurrence_of_min(df, axis=0))  # find first occurrence of minimum along rows
print(get_first_occurrence_of_min(df, axis=1))  # find first occurrence of minimum along columns
