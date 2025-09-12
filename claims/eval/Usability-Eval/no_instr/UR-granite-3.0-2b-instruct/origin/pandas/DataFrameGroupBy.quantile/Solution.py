import pandas as pd

def get_quantile(series, quantile):
    return series.quantile(quantile)

# Example usage:
data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(get_quantile(data, 0.5))  # Output: 5.5
