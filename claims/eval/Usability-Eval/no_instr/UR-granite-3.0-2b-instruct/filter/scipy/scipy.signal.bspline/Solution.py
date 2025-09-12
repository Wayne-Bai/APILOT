import numpy as np
from scipy.special import bondary

def bspline_basis_function(n, x):
    knot_vector = np.linspace(0, 1, n+1)
    basis = bondary(n, x, knot_vector)
    return basis
