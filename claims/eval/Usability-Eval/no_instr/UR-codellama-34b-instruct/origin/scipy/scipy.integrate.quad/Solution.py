
import numpy as np
from scipy.integrate import quad

def integrand(x):
    return x**2 + 1

result = quad(integrand, 0, 4)
print(result)
