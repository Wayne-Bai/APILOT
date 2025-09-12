
import numpy as np
from scipy.integrate import odeint

# Define the continuous-time linear system
def linear_system(x, t):
    A = np.array([[-2, -1], [1, -1]])  # Sample system matrix
    dxdt = np.dot(A, x)
    return dxdt

# Initial condition
x0 = np.array([1, 0])

# Time points to simulate the system
t = np.linspace(0, 5, 100)  # Start at 0, end at 5, 100 time points

# Solve the ODE for the linear system
x = odeint(linear_system, x0, t)

print(x)
