import numpy as np
from scipy.interpolate import BSpline

def evaluate_bspline_basis(order, num_points=100):
    k = order  # Order of the B-spline
    t = np.concatenate(([0] * k, np.linspace(0, 1, num_points - 2 * k + 2), [1] * k))  # Knot vector
    c = np.zeros(len(t) - k - 1)  # Coefficients (only one is 1, rest are 0)
    x = np.linspace(0, 1, num_points)

    # Generate B-spline basis functions
    basis_functions = []
    for i in range(len(c)):
        c[:] = 0
        c[i] = 1
        spline = BSpline(t, c, k)
        basis_functions.append(spline(x))

    return x, basis_functions

# Example usage
x, basis_functions = evaluate_bspline_basis(3)
for i, b in enumerate(basis_functions):
    plt.plot(x, b, label=f'Basis {i+1}')

plt.legend()
plt.show()
