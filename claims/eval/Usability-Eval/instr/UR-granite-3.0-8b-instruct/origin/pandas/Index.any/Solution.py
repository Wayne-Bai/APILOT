import pandas as pd

def check_truthy(df):
    return df.apply(lambda x: bool(x.astype(bool).any()))

# Example usage:
df = pd.DataFrame({'A': [1, 2, 0], 'B': [False, True, None]})
print(check_truthy(df))
