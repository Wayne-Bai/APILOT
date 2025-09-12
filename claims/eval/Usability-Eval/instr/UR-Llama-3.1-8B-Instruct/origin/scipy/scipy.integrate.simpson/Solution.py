import numpy as np
from scipy import integrate

def composite_simpsons_rule(y_values, axis=None, dx=None):
    """
    Integrate y(x) using samples along the given axis and the composite Simpson’s rule.

    Parameters:
    y_values (array): Values of y
    axis (None or int, optional): Axis along which to integrate. If None (default), integrate over all of the axes.
    dx (None or float, optional): Spacing between samples. If None, automatically calculate it.

    Returns:
    result (float or array): Result of integration (one value for one-dimensional case, or array for multi-dimensional case)
    """

    # If dx is None, calculate it as the average spacing between samples
    if dx is None:
        dx = np.mean(np.diff(y_values))

    # Create a grid of x values by assuming the y_values are equispaced
    x_values = np.arange(len(y_values)) * dx

    # Rotate the axes so that the axis to integrate is the first one
    y_values = np.rot90(y_values, 2)

    # Create a quad object from the grid of x and y values
    result, _ = integrate.quad(lambda x: integrate.trapz(y_values[:, x], dx=dx), 0, len(y_values[0]) - 1)

    return result

# Example usage:
y_values = np.array([1, 4, 9, 16, 25])
result = composite_simpsons_rule(y_values)
print(result)

