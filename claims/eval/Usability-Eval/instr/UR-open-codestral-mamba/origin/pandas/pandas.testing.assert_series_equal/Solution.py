import pandas as pd

def check_like(series1, series2):
    """
    This function takes 2 pandas series and checks whether each element is the same or not.
    It works the same as the assert method but provides clearer and more detailed messages.
    """

    # Check if both series have the same length
    if len(series1) != len(series2):
        return False

    for i in range(len(series1)):
        # Check if each value is the same
        if series1.iloc[i] != series2.iloc[i]:
            return False

    return True

# Let's test the function with some series
series1 = pd.Series([1, 2, 3, 4, 5])
series2 = pd.Series([1, 2, 3, 6, 5])
print(check_like(series1, series2)) # prints False

series3 = pd.Series([1, 2, 3, 4, 5])
series4 = pd.Series([1, 2, 3, 4, 5])
print(check_like(series3, series4)) # prints True
