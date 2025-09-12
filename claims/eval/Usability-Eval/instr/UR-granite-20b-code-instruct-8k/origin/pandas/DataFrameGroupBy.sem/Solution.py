import pandas as pd

def compute_standard_error(data, group_by):
    return data.groupby(group_by).transform('std').mean()
