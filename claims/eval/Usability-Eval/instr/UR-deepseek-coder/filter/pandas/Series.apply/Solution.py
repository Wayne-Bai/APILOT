import pandas as pd

# Example Series
data = [10, 20, 30, 40, 50]
series = pd.Series(data)

# Define a function to apply to each value in the Series
def custom_function(x):
    return x * 2

# Apply the function to the Series
result_series = series.apply(custom_function)

print(result_series)
