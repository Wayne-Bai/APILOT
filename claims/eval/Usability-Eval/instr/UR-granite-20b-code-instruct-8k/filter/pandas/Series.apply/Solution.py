import pandas as pd

# create a Series
s = pd.Series([1, 2, 3, 4, 5])

# define a function to be invoked on the values of the Series
def square(x):
    return x**2

# invoke the function on the values of the Series using the apply() method
result = s.apply(square)

# print the result
print(result)
