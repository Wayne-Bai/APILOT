import numpy as np
from scipy.integrate import odeint

# Define the differential equation
def dx_dt(x, t):
    A = np.array([[1, -2], [3, -4]])
    B = np.array([[1], [2]])
    return np.dot(A, x) + np.dot(B, np.sin(t))

# Initial conditions
x0 = np.array([0, 1])
t = np.linspace(0, 10, 1000)

# Solve the differential equation
sol = odeint(dx_dt, x0, t)

# Print the output
print(sol)
