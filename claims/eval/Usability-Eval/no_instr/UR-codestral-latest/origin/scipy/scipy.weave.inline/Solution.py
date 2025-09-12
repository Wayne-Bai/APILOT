import numpy as np
from scipy import special

# Using Bessel function of first kind, order 0
x = np.linspace(0, 10, 500)
y = special.jv(0, x)

print(y)
