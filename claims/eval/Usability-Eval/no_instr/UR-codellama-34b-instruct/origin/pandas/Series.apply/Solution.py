
import pandas as pd

# create a sample series
s = pd.Series([1, 2, 3, 4, 5])

# define a function to perform the operation
def op(x):
    return x ** 2

# apply the function on the values of the series
result = s.apply(op)

print(result)
