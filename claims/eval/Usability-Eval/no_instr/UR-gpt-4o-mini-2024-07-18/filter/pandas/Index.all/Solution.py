import pandas as pd

def all_elements_truthy(series):
    return series.all()

# Example usage
data = pd.Series([1, 2, 3, 4, 5])
result = all_elements_truthy(data)
print(result)  # Output: True
