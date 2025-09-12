import scipy
from scipy.optimize import shgo

def function(x):
    # Define your function here
    return x**2

result = shgo(function, bounds=[(-10, 10), (-10, 10)])
print(result)
