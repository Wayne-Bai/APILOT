from scipy import integrate
import numpy as np

def integrate_simpsons(y, x=None, axis=-1, dx=1.0, even='avg'):
    """
    Integrate y(x) using samples along the given axis and the composite Simpson’s rule.
    
    Parameters:
    y : array_like
        Array to be integrated.
    x : array_like, optional
        If given, the points at which y is sampled.
    axis : int, optional
        Axis along which to integrate. Default is the last axis.
    dx : scalar, optional
        Spacing of integration points along axis, can be used if x is None. Default is 1.
    even : {‘avg’, ‘first’, ‘last’}, optional
        Control rounding of the result when there are an odd number of samples.
    
    Returns:
    simps : float
        The result of the integration.
    """
    return integrate.simpson(y, x=x, axis=axis, dx=dx, even=even)

# Example usage
y_samples = np.array([1, 2, 3, 4, 5])
integration_result = integrate_simpsons(y_samples)
print("Integration result:", integration_result)
