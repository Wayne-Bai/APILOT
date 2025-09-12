import pandas as pd

# Suppose we have a DataFrame `df`
# We can check if any element in the DataFrame is truthy using the `any` method
# This will return True if there is at least one True or non-empty value in the DataFrame

is_any_truthy = df.any().any()
print(is_any_truthy)
