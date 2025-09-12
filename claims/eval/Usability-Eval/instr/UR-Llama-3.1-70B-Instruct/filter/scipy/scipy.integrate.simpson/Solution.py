import scipy.integrate as integrate
import numpy as np

def integrate_using_simpsons_rule(y, x=None, dx=1, axis=-1):
    """
    Integrate y(x) using samples along the given axis and the composite Simpson’s rule.

    Parameters:
    y (array_like): Array to integrate.
    x (array_like, optional): If given, the points at which `y` is sampled.
    dx (float, optional): Spacing of x values if x is not given.
    axis (int, optional): Axis in y along which to integrate.

    Returns:
    The integral of `y` (and `x` if given).
    """
    return integrate.simpson(y, x, dx, axis)

# Example usage:
y = np.array([1, 4, 9, 16])
x = np.array([0, 1, 2, 3])

# Use the simpson's rule to integrate
result = integrate_using_simpsons_rule(y, x)

print("The integral is: ", result)

# Without providing x, dx is assumed
result_without_x = integrate_using_simpsons_rule(y)

print("The integral is: ", result_without_x)
