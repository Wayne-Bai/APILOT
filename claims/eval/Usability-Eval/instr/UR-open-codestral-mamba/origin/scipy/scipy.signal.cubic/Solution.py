from scipy.special import comb
import numpy as np

def cubic_bspline(x, knots, coef):
    # Assume that x is a sorted array of x values
    # knots are the knot values in increasing order
    # coef are the coefficients defining the shape of the curve

    # Compute the basis functions
    basis = np.zeros((len(knots)-4, len(x)))
    for i in range(2, len(knots)-1):
        for j, x_val in enumerate(x):
            if x_val < knots[i] or x_val >= knots[i+1]:
                continue
            basis[i-2, j] = comb(3, 0) * ((knots[i] - x_val)**3) / 6 \
                          + comb(3, 1) * ((x_val - knots[i-1])**3) / 6

    # Compute the curve as a linear combination of the basis functions
    return np.dot(coef, basis)
