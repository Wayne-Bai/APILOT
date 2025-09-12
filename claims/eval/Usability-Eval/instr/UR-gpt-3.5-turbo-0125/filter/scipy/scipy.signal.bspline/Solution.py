
import numpy as np

def basis_function(t, i, k, knots):
    if k == 0:
        if knots[i] <= t < knots[i+1] or (i == len(knots)-2 and t == knots[i+1]):
            return 1
        else:
            return 0
    else:
        result = 0
        if knots[i+k] != knots[i]:
            result += (t - knots[i]) / (knots[i+k] - knots[i]) * basis_function(t, i, k-1, knots)
        if knots[i+k+1] != knots[i+1]:
            result += (knots[i+k+1] - t) / (knots[i+k+1] - knots[i+1]) * basis_function(t, i+1, k-1, knots)
        return result
    
def bspline_basis(t, k, knots):
    n = len(knots) - k - 1
    return np.array([basis_function(t, i, k, knots) for i in range(n)])

# Example usage:
knots = [0, 0, 0, 1, 2, 3, 4, 4, 5, 5, 5]
order = 2
t_val = 3.5
result = bspline_basis(t_val, order, knots)
print(result)
