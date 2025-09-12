
from scipy import integrate

def integrate_y(y, x=None, dx=None):
    if x is not None:
        # Use Simpson's rule with composite trapezoidal rule
        return integrate.simps(y, x, dx)
    else:
        # Use Simpson's rule with sample spacing of dx
        return integrate.simps(y, dx=dx)
