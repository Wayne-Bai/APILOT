import pandas as pd

def get_quantiles(data, axis=0, quantiles=[0.25, 0.75]):
    if axis == 0:
        return data.quantile(quantiles)
    elif axis == 1:
        return data.T.quantile(quantiles).T
    else:
        raise ValueError("Axis must be 0 or 1")

# Example usage:
data = pd.Series([1, 2, 3, 4, 5])
quantiles = get_quantiles(data, axis=0, quantiles=[0.25, 0.5, 0.75])
print(quantiles)
