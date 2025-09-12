import pandas as pd

def suffix_labels_with_string(df, suffix):
    new_labels = {col: col + suffix for col in df.columns}
    df.rename(columns=new_labels, inplace=True)
    return df
