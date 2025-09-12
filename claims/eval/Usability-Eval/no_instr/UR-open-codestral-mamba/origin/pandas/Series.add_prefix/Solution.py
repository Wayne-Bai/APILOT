import pandas as pd

def prefix_labels(df, prefix):
    """Prefix labels with a given string."""
    df.columns = [f'{prefix}_{col}' for col in df.columns]
    return df

# Example usage:
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

prefixed_df = prefix_labels(df, 'pre')
print(prefixed_df)
