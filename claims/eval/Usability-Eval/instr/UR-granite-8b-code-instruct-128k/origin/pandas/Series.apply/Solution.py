
import pandas as pd

# create a Series
s = pd.Series([1, 2, 3, 4, 5])

# define a function to be applied to the values
def func(x):
    return x * 2

# apply the function to the values of the Series
result = s.apply(func)

# print the result
print(result)
