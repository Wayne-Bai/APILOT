import pandas as pd

def find_first_occurrence_of_max(df, axis=0):
    """
    Return index of first occurrence of maximum over requested axis.
    
    Parameters:
    df (pandas.DataFrame): The input dataframe.
    axis (int): The axis to search for the maximum. Defaults to 0 (rows).
    
    Returns:
    pandas.Index: The index of the first occurrence of the maximum.
    """
    
    # Find the index of the maximum value
    if axis == 0:
        max_idx = df.loc[df.eq(df.max()).all(axis=1)].index[0]
    elif axis == 1:
        max_idx = df.eq(df.max().repeat(df.shape[0])).idxmax(axis=1).iloc[0]
    
    return max_idx

# Example usage
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [6, 7, 8, 9, 10]
})

print(find_first_occurrence_of_max(df))  # Find the first occurrence of maximum in the entire dataframe

df.loc['C', 'A'] = 2
df.loc['D', 'A'] = 3
print(find_first_occurrence_of_max(df, axis=0))  # Find the first occurrence of maximum in rows

df.set_index('A', inplace=True)
print(find_first_occurrence_of_max(df, axis=0)) # Find the first occurrence of maximum in rows
