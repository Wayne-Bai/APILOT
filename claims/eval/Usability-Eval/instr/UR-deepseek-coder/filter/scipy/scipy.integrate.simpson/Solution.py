import numpy as np
from scipy.integrate import simpson

def integrate_simpson(y, x=None, dx=1.0, axis=-1):
    """
    Integrate y(x) using samples along the given axis and the composite Simpson’s rule.

    Parameters:
    y : array_like
        Array to be integrated.
    x : array_like, optional
        The sample points corresponding to the y values. If x is None, the sample points are assumed to be evenly spaced dx apart.
    dx : float, optional
        The spacing between sample points when x is None. Default is 1.0.
    axis : int, optional
        The axis along which to integrate. Default is -1.

    Returns:
    float
        The computed integral.
    """
    if x is None:
        return simpson(y, dx=dx, axis=axis)
    else:
        return simpson(y, x=x, axis=axis)

# Example usage:
# y = np.array([1, 4, 1])
# x = np.array([0, 1, 2])
# result = integrate_simpson(y, x)
# print(result)  # Output: 4.0
