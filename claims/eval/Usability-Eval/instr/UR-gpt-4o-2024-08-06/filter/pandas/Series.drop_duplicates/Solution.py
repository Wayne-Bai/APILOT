import pandas as pd

# Function to remove duplicate values from a Pandas Series
def remove_duplicates_from_series(series):
    # Creating a new Series with duplicates removed
    unique_series = series[~series.duplicated()]
    return unique_series

# Example usage
data = pd.Series([1, 2, 2, 3, 4, 5, 5, 6])
result = remove_duplicates_from_series(data)
print(result)
