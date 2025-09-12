import pandas as pd

def test_series_equal(series1, series2, check_like=True):
    """
    Test if two pandas Series are equal.

    Args:
    series1 (pandas Series): The first series to compare.
    series2 (pandas Series): The second series to compare.
    check_like (bool, optional): If True (default), check if the two series have the same shape and data type. 
                                 If False, only check if the values of the two series are equal.

    Returns:
    None
    """
    try:
        if check_like:
            assert series2.equals(series1)
        else:
            assert (series1 == series2).all()
    except AssertionError as e:
        print(f"Series are not equal: {e}")

# Create two sample series
series1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
series2 = pd.Series([1, 2, 4], index=['a', 'b', 'c'])
series3 = pd.Series([1.0, 2.0, 3.0], index=['a', 'b', 'c'])

# Test the series
test_series_equal(series1, series2)  # check_like=True by default
test_series_equal(series1, series2, check_like=False)  # check_like=False
test_series_equal(series1, series3)  # Different data types
