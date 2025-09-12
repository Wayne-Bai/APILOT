import pandas as pd

def get_quantile(data, quantile):
    return data.quantile(quantile)

# Example usage:
data = pd.Series([1, 2, 3, 4, 5])
quantile = 0.5
print(get_quantile(data, quantile))
