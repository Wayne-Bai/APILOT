import pandas as pd

def remove_duplicates(series):
    seen = set()
    result = []
    for value in series:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return pd.Series(result)

# Example usage:
# series = pd.Series([1, 2, 2, 3, 4, 4, 5])
# unique_series = remove_duplicates(series)
# print(unique_series)
