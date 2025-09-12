import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x, a, b, c):
    """
    The function to fit the data to.
    
    Parameters:
    a (float): The amplitude of the function.
    b (float): The frequency of the function.
    c (float): The phase of the function.
    
    Returns:
    float: The function value at x.
    """
    return a * np.sin(b * x + c)

# Generate some noisy data
x = np.linspace(0, 10, 100)
y = f(x, 1.0, 0.5, 1.0) + np.random.normal(0, 0.1, 100)

# Initial guess for the parameters
p0 = [1.0, 0.5, 1.0]

# Bounds for the parameters
bounds = [(0, None), (0, None), (0, 2*np.pi)]

# Perform the fit
result = opt.least_squares(lambda p: f(x, *p) - y, p0, bounds=bounds)

# Print the fitted parameters
print("Fitted parameters:", result.x)

# Plot the data and the fitted function
plt.plot(x, y, 'bo', label='data')
plt.plot(x, f(x, *result.x), 'r-', label='fit')
plt.legend()
plt.show()
