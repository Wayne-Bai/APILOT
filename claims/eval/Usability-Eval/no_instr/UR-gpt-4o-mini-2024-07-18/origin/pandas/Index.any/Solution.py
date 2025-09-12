import pandas as pd

def is_any_truthy(data):
    return pd.Series(data).any()

# Example usage
data = [0, '', [], {}, None, 1]
result = is_any_truthy(data)
print(result)  # Output: True
