import numpy as np

def bspline_basis(k, t, i, n):
    """
    Compute B-spline basis function of order n at position t[i]
    
    Parameters:
    k (int): Order of the B-spline
    t (np.ndarray): Knot sequence
    i (int): Index of the point to evaluate the basis function
    n (int): Degree of the polynomial in the B-spline
    
    Returns:
    float: Value of the basis function at position t[i]
    """
    
    if k == 0:
        # Base case: if k is 0, return 1 if the current point is one of the knots, otherwise return 0
        return 1 if t[i] == t[k] else 0
    else:
        # Recursive case: if k is greater than 0, compute the basis function using the formula:
        # N_{i,k}(t) = (t - t_{i}) / (t_{i+k} - t_{i}) * N_{i,k-1}(t) + (t_{i+k+1} - t) / (t_{i+k+1} - t_{i}) * N_{i+1,k-1}(t)
        return ((t[i+k] - t[i]) / (t[i+k] - t[i-1]) * bspline_basis(k-1, t, i-1, n) + (t[i+k+1] - t[i]) / (t[i+k+1] - t[i]) * bspline_basis(k-1, t, i, n)) if t[i+k]!= t[i+k+1] else bspline_basis(k-1, t, i, n)

# Example usage:
knots = np.array([0, 0, 2, 4, 4, 6, 8, 8])
degree = 2
order = degree + 1
print(bspline_basis(order, knots, 2, degree))
