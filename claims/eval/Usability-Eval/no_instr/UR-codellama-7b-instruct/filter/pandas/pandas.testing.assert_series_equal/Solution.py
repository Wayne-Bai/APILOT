
import pandas as pd

# define a function that checks for missing values in a series
def check_like(series1, series2):
    # check if both series have the same index and values
    assert series1.index == series2.index
    assert series1.values == series2.values
    
    # check if any of the indices are nan or inf in both series
    for idx in series1.index:
        if pd.isna(series1[idx]) or pd.isinf(series1[idx]):
            assert pd.isna(series2[idx]) or pd.isinf(series2[idx])
    
    # check if any of the values are nan or inf in both series
    for val in series1.values:
        if pd.isna(val) or pd.isinf(val):
            assert pd.isna(series2[series1.index[series1.values == val]]) or pd.isinf(series2[series1.index[series1.values == val]])
            
# use the function to check for missing values in two series
check_like(pd.Series([1, 2, 3, np.nan]), pd.Series([1, 2, 4, np.nan]))
