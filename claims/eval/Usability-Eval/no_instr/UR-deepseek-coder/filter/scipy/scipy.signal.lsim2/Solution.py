import numpy as np
from scipy.integrate import odeint

# Define the system of ODEs
def linear_system(y, t, A, B, u):
    # y is the state vector, t is time, A is the state matrix, B is the input matrix, u is the input vector
    dydt = np.dot(A, y) + np.dot(B, u(t))
    return dydt

# Define the system parameters
A = np.array([[-1, 2], [0, -2]])  # State matrix
B = np.array([[1], [1]])          # Input matrix

# Define the input function
def input_function(t):
    return np.array([np.sin(t)])

# Initial conditions
y0 = np.array([1, 0])

# Time points
t = np.linspace(0, 10, 100)

# Solve the ODE
solution = odeint(linear_system, y0, t, args=(A, B, input_function))

# Extract the state variables
x1, x2 = solution.T

# Print the results
print("Time points:", t)
print("State variable x1:", x1)
print("State variable x2:", x2)
