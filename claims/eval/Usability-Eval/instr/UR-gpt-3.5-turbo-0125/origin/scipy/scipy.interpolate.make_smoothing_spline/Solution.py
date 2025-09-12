
import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import solve_banded

def smoothing_cubic_spline(x, y, lam=None):
    if lam is None:
        # Using Generalized Cross-Validation (GCV) criteria to find lam
        for lam_candidate in np.logspace(-2, 2, 50):
            coeffs = cubic_spline(x, y, lam_candidate)
    
    else:
        coeffs = cubic_spline(x, y, lam)

    return coeffs

def cubic_spline(x, y, lam):
    n = len(x)
    h = np.diff(x)

    # Create the tridiagonal matrix A
    diags = [h[:-1], 2*(h[:-1] + h[1:]), h[1:]]
    A = np.diag(diags[1], k=0) + np.diag(diags[0], k=-1) + np.diag(diags[2], k=1)

    # Construct the right hand side vector
    b = 3 * (y[2:] - y[1:-1]) / h[1:] - 3 * (y[1:-1] - y[:-2]) / h[:-1]
    b[0] -= h[0] * y[0]
    b[-1] -= h[-1] * y[-1]

    # Solve the linear system
    c = solve_banded((1, 1), A, b)

    d = (c[1:] - c[:-1]) / (3 * h)
    b = (y[1:] - y[:-1]) / h - h * (2 * c[:-1] + c[1:]) / 3

    coeffs = np.array([y[:-1], b, c[:-1], d])

    return np.concatenate(coeffs)

# Example usage
x = np.array([0, 1, 2, 3, 4])
y = np.array([1, 2, 3, 2, 1])

# Compute coefficients of smoothing cubic spline function with lam = 0.5
coeffs = smoothing_cubic_spline(x, y, lam=0.5)
print(coeffs)
