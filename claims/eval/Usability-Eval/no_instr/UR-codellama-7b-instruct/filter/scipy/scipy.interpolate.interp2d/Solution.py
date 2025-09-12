
import numpy as np
from scipy import interpolate

def interpolate_2d(x, y, z):
    # Create a 2D grid
    x_grid = np.linspace(start=x.min(), stop=x.max(), num=len(x))
    y_grid = np.linspace(start=y.min(), stop=y.max(), num=len(y))
    X, Y = np.meshgrid(x_grid, y_grid)

    # Interpolate over the 2D grid
    interpolator = interpolate.interp2d(x, y, z, kind='linear')
    Z = interpolator(X, Y)

    return Z
