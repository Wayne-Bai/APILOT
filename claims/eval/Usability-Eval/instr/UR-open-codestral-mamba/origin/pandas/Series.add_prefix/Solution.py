import pandas as pd

def prefix_labels(df, prefix):
    df.columns = [f'{prefix}_{col}' for col in df.columns]
    return df

# Example usage
df = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(prefix_labels(df, 'my_prefix'))
