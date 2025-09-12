import pandas as pd

def check_any_truthy(data):
    return data.any()

# Example usage
data = pd.Series([0, None, False, 1, 'string'])
result = check_any_truthy(data)
print(result)  # Output: True
