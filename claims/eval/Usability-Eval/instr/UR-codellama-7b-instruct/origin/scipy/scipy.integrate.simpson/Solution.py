
import numpy as np
from scipy.integrate import simps

def integrate_y_using_simpsons_rule(y, x, n=None):
    """Integrate y(x) using Simpson's rule with composite trapezoidal rule."""
    if x is None:
        dx = 1.0
    else:
        dx = np.diff(x)

    # Compute the integral using Simpson's rule with composite trapezoidal rule
    I = simps(y * dx, dx=dx)

    return I
