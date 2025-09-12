from scipy.special import comb

def bspline_basis_function(n, i, x, knots):
    if i < 0 or i >= n + 1:
        return 0

    if x < knots[i] or x > knots[i + 1]:
        return 0

    if i == 0:
        return 1

    if i == n:
        return (x - knots[i - 1]) / (knots[i] - knots[i - 1])

    return (x - knots[i - 1]) / (knots[i] - knots[i - 1]) * bspline_basis_function(n, i - 1, x, knots) + \
           (knots[i + 1] - x) / (knots[i + 1] - knots[i]) * bspline_basis_function(n, i, x, knots)

# Example usage:
n = 3
knots = [0, 1, 2, 3, 4]
x = 1.5
print(bspline_basis_function(n, 1, x, knots))
