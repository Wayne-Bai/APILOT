from scipy.interpolate import BSpline
import numpy as np
import matplotlib.pyplot as plt

def b_spline_basis(knots, coefficients, degree):
    """
    Create a B-spline basis function of given degree.

    :param knots: A non-decreasing sequence of real numbers representing the knots.
    :param coefficients: An array of coefficients for the spline basis.
    :param degree: The degree of the B-spline.
    :return: A function that represents the B-spline basis.
    """
    # Create a B-spline basis
    b_spline = BSpline(knots, coefficients, degree)
    return b_spline

# Example usage
# Knots vector should have m = n + 1 + degree + 1 elements
knots = np.array([0, 1, 2, 3, 4, 5, 6])
# Coefficients setting for a specific basis function, must match with n + degree + 1 num_knots - (2*degree) - 1
coefficients = np.array([0, 0, 1, 0, 0, 0, 0])
degree = 2

# Creating a B-spline basis function
b_spline = b_spline_basis(knots, coefficients, degree)

# Plotting the B-spline basis function
x = np.linspace(knots[0], knots[-1], 100)
plt.plot(x, b_spline(x), label='B-spline basis')
plt.title('B-spline Basis Function')
plt.xlabel('x')
plt.ylabel('B-spline')
plt.grid()
plt.legend()
plt.show()
