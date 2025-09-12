import numpy as np
from scipy.integrate import simps

def integrate_y_using_samples(x, y, axis=None, dx=None):
    if dx is None:
        dx = np.diff(x)
    if axis is None:
        axis = len(y.shape) - 1
    y_sampled = np.resize(y, (dx.size, *dx.size))
    y_sampled[:, ::2] = y
    y_sampled[:, 1::2] = y
    y_sampled = np.mean(y_sampled, axis=axis)
    return simps(y_sampled, dx=dx, even='avg')
