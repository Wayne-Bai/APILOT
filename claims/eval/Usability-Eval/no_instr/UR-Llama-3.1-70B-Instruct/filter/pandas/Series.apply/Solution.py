import pandas as pd

# Create a sample Series
series = pd.Series([1, 2, 3, 4, 5])

# Define a function to be invoked on the values of the Series
def square(x):
    return x ** 2

# Invoke the function on the values of the Series using apply()
result = series.apply(square)

print("Original Series:")
print(series)
print("\nResult after applying the function:")
print(result)
