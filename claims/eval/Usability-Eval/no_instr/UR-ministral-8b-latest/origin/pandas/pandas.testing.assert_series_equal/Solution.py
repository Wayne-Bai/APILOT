import pandas as pd

def check_series_equal(series1, series2, check_like=False):
    if check_like:
        # Compare data frames while allowing for differences in order
        return series1.compare(series2, aligned=False)
    else:
        # Compare data frames while enforcing order
        return series1.equals(series2)

# Sample data to test the function
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'B': [4, 5, 6], 'A': [1, 2, 3]})
df3 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 0]})

series1 = df1['A']
series2 = df2['A']
series3 = df3['A']

# Test with same order
assert check_series_equal(series1, series2)

# Test without allow order
assert check_series_equal(series1, series3, check_like=True)
