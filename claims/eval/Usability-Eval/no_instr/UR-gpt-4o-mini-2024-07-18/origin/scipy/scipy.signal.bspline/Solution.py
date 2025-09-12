import numpy as np
from scipy.interpolate import BSpline, make_interp_spline

def b_spline_basis(order, knots, n_points=100):
    # Create the B-spline basis functions
    degree = order - 1
    # Create a B-spline object
    spline = BSpline(knots, np.identity(len(knots) - degree - 1), degree)
    
    # Generate points for plotting the basis functions
    x = np.linspace(knots[degree], knots[-degree - 1], n_points)
    basis_values = [spline(x, k) for k in range(len(knots) - degree - 1)]

    return x, basis_values

# Example usage
order = 3
knots = [0, 0, 0, 1, 2, 2, 2]  # Example knots
x_values, basis_functions = b_spline_basis(order, knots)

# To visualize the results (optional)
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
for basis in basis_functions:
    plt.plot(x_values, basis, label='Basis Function')
plt.title('B-spline Basis Functions of Order {}'.format(order))
plt.xlabel('x')
plt.ylabel('B-spline value')
plt.legend()
plt.grid()
plt.show()
