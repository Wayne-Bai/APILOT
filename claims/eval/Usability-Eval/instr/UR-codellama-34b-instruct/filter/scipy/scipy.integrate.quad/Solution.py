
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return x**2 + 1

a = 0
b = 1
result, error = quad(integrand, a, b)
print(f"Result: {result}, Error: {error}")
