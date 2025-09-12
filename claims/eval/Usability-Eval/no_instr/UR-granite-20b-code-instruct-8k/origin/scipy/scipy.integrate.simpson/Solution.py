import scipy
def integrate_simpson(y, x=None, dx=1, axis=-1):
    return scipy.integrate.simpson(y, x, dx, axis)
