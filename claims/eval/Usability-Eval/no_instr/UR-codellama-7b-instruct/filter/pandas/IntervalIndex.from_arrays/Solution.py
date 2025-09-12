
import pandas as pd

# constructing a list of tuples from two arrays defining the left and right bounds
left_bounds = [1, 2, 3, 4, 5]
right_bounds = [2, 3, 4, 5, 6]

# creating a pandas Series using the arrays
s = pd.Series(left_bounds + right_bounds)

# using the 'rolling' function to calculate the difference between consecutive elements
result = s.rolling(window=2).apply(lambda x: x[1] - x[0], raw=True)

print(result)
