import pandas as pd

def pivot_index_level(df, level):
    # Function to pivot a level of the hierarchical index labels
    df_pivoted = df.pivot(columns=level)
    return df_pivoted

# Example usage:
# Assuming you have a DataFrame `df` with a hierarchical index:
# indices = pd.MultiIndex.from_tuples([(1, 'a', 'x'), (1, 'a', 'y'), (1, 'b', 'x'), (1, 'b', 'y')])
# df = pd.DataFrame(columns=['col1', 'col2'], index=indices)

# level = 'a'  # The level you want to pivot
# df_pivoted = pivot_index_level(df, level)
# print(df_pivoted)
