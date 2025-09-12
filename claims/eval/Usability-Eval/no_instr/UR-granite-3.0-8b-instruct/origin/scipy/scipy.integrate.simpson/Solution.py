import numpy as np
from scipy.integrate import simps

def simpson_rule_integration(y, x=None, dx=None):
    if x is None and dx is None:
        raise ValueError("Either x or dx must be provided.")
    if x is not None:
        dx = x[1] - x[0]
    return simps(y, dx=dx)
