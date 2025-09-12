from scipy.interpolate import bspline
import numpy as np

x = np.linspace(0, 1, 10)
y = bspline(x, 2)

print(y)
