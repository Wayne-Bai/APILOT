
import numpy as np

def bspline_basis_function(t, i, k, knots):
    if k == 0:
        if knots[i] <= t < knots[i+1] or (i == len(knots) - 2 and t == knots[i+1]):
            return 1.0
        else:
            return 0.0
    else:
        term1 = 0.0
        term2 = 0.0

        if knots[i+k] - knots[i] != 0:
            term1 = (t - knots[i]) / (knots[i+k] - knots[i]) * bspline_basis_function(t, i, k-1, knots)

        if knots[i+k+1] - knots[i+1] != 0:
            term2 = (knots[i+k+1] - t) / (knots[i+k+1] - knots[i+1]) * bspline_basis_function(t, i+1, k-1, knots)

        return term1 + term2

# Example usage
k = 3  # Order of the B-spline basis function
knots = [0, 0, 0, 1, 2, 3, 4, 4, 4]  # Example knot vector
t = 2.5  # Evaluation point

# Calculate B-spline basis function values at t
basis_values = [bspline_basis_function(t, i, k, knots) for i in range(len(knots)-k-1)]

print(basis_values)
