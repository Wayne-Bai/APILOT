
import numpy as np
from scipy.optimize import approx_derivative

# Define the function for which the gradient correctness will be checked
def my_function(x):
    return 0.5 * np.sum(x**2)

# Define the gradient of the function manually
def my_gradient(x):
    return x

# Generate a random initial point to evaluate the gradients
x0 = np.random.rand(5)

# Use the approx_derivative function to calculate the gradient approximation
grad_exact = my_gradient(x0)
grad_approx = approx_derivative(my_function, x0)

# Calculate the error between the exact gradient and the approximated gradient
error = np.linalg.norm(grad_exact - grad_approx)

print("Error between the exact gradient and the approximated gradient:", error)
