import numpy as np
from scipy.integrate import composite_simps

def integrate_y_using_simpsons_rule(x, y):
    if x is None:
        x = np.linspace(0, 1, len(y))
    return composite_simps(y, x)
