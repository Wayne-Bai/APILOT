import numpy as np
from scipy.integrate import quad
from scipy.special import hermite

def hermite_spline(x, order):
    return np.array([hermite(i)(x) for i in range(order)])

def approximated_inverse_cdf(cdf, order=10):
    def inverse_cdf_x(x):
        return x

    def Hermite_basis(x, order):
        return hermite_spline(x, order)

    # Initialize the higher-order polynomials:
    coeffs = np.zeros(order + 1)
    z = cdf()  # CDF sample point

    # Compute higher-order polynomials:
    integral = 0
    for i in range(order + 1):
        if i == 0:
            integral = z
        else:
            integral += (z ** i) / (order + i)
        coeffs[i] = integral

    # Define the Hermite spline:
    spline = Hermite_basis(z, order)

    def apply_spline(basis_values):
        return np.dot(basis_values, np.array(coeffs)) - z

    # Approximate the inverse CDF:
    def inverse_cdf(x):
        cdf_val = np.dot(apply_spline(spline), hermite_spline(x, order))
        return cdf_val

    return inverse_cdf

# Example usage:
# Define your CDF function
def cdf_function(x):
    return np.sin(x)  # Example CDF function

order = 5
inv_cdf = approximated_inverse_cdf(cdf_function, order)

x_vals = np.linspace(0, np.pi, 100)
y_vals = inv_cdf(x_vals)

import matplotlib.pyplot as plt
plt.plot(x_vals, y_vals)
plt.title('Approximated Inverse CDF using Hermite Spline')
plt.xlabel('x')
plt.ylabel('Approximated CDF Inverse Value')
plt.grid(True)
plt.show()
