import numpy as np
from scipy.integrate import simps

def integrate_y_with_simps(y, x=None, dx=None):
    if x is None or dx is None:
        nn = 100  # default number of samples
        x = np.linspace(0, 1, nn)
        dx = (1 - 0) / (nn - 1)
    else:
        nn = len(x)
    ri = 0.5 * dx if x[0] != x[1] else dx
    return simps(y, x, dx=ri)

# Example usage:
x = np.linspace(0, 1, 20)
y = np.sin(x)
result = integrate_y_with_simps(y, x=x)
print(result)
