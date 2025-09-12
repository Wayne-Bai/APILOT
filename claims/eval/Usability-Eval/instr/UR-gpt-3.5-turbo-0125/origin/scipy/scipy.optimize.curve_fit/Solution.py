
import numpy as np
from scipy import optimize

# Define the function to fit
def f(x, a, b, c):
    return a * np.sin(b * x) + c

# Generate sample data
x_data = np.linspace(0, 10, 100)
y_data = f(x_data, 3, 2, 1) + 0.5 * np.random.normal(size=x_data.size)

# Define the loss function
def loss(params):
    return y_data - f(x_data, *params)

# Perform the non-linear least squares fit
initial_guess = [1, 1, 1]
params, _ = optimize.leastsq(loss, initial_guess)

print("Fitted parameters:", params)
