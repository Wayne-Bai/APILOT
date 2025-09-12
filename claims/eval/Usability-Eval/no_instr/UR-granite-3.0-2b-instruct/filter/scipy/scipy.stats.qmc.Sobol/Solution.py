import numpy as np
from scipy.special import i0, i1
from scipy.stats import norm

def sobol_generate(dim, points):
    "Generates Sobol' sequences using the Gauss-Legendre method"
    # Generate Gauss-Legendre points
    x = norm.ppf(np.random.rand(points))
    w = np.random.rand(points)

    # Compute the Jacobi polynomials
    P = np.zeros((dim, points))
    for i in range(dim):
        P[i, :] = i0(i + 1) * np.poly1d(np.polyfit(x, w, i + 1))

    # Compute the Sobol' sequences
    sobol = np.zeros((dim, points))
    for i in range(dim):
        sobol[i, :] = P[i, :] / i1(i)

    return sobol
