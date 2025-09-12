import pandas as pd
def get_elements(df, axis, *args):
    return df.iloc[args, :] if axis == 0 else df.iloc[:, args]
