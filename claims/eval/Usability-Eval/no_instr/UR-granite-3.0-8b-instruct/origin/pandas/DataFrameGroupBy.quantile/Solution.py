import pandas as pd

def quantile_group(df, group_by, quantile):
    return df.groupby(group_by).apply(lambda x: x.quantile(quantile))
