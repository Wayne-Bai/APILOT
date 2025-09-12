# Import necessary libraries
from scipy import integrate
import numpy as np

# Define a function to integrate
def integrand(x):
    """
    Function to integrate.
    
    Parameters:
    x (float or numpy array): Input value(s)
    
    Returns:
    float or numpy array: Result of the function evaluation
    """
    return x**2 + 3*x + 2

# Define the limits of integration
a = 0  # Lower limit
b = 4  # Upper limit

# Compute the definite integral
result, error = integrate.quad(integrand, a, b)

# Print the result and error
print(f"The definite integral is: {result}")
print(f"The estimated error is: {error}")

# If you want to plot the function and the area under the curve, you can use matplotlib
import matplotlib.pyplot as plt

x = np.linspace(a, b, 400)
y = integrand(x)

plt.fill_between(x, 0, y, alpha=0.3)
plt.plot(x, y, label='y = x^2 + 3x + 2')
plt.xlim(a, b)
plt.ylim(0, max(y) * 1.1)
plt.title('Definite Integral of y = x^2 + 3x + 2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()
