import pandas as pd

def remove_duplicates(series):
    return series.drop_duplicates()

# Example usage
data = pd.Series([1, 2, 2, 3, 4, 4, 5])
series_without_duplicates = remove_duplicates(data)
print(series_without_duplicates)
