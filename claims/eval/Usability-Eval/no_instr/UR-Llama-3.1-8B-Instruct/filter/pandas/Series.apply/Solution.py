# Import the pandas library
import pandas as pd

# Create a pandas series
series = pd.Series([1, 2, 3, 4, 5])
print("Original Series:")
print(series)

# Define a function to double the values in the series
def double_values(x):
    return x * 2

# Use the apply function to invoke the function on each value in the series
doubled_series = series.apply(double_values)
print("\nSeries with doubled values:")
print(doubled_series)
