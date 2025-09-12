import pandas as pd

# Define the series
s = pd.Series([20, 21, 12, 18, 24])

# Define a custom function to apply
def custom_function(x):
    return x * 2 + 3

# Invoke the function on the series values using 'apply' method
result_series = s.apply(custom_function)

# Display the result
print(result_series)
