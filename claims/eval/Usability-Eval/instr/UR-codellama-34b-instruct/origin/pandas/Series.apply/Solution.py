
import pandas as pd

# create a sample series
s = pd.Series([1, 2, 3])

# define a function to square each value
def square(x):
    return x**2

# use the apply() method to invoke the square function on each value of the series
squared_series = s.apply(square)

print(squared_series)  # prints Series([1, 4, 9])
