import pandas as pd

def quantile_groups(data, groups, quantile):
    return data.groupby(groups).quantile(quantile)
