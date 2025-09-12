import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system
def linear_system(x, t, A, b):
    dxdt = np.dot(A, x) + b
    return dxdt

# System parameters
A = np.array([[0, 1], [-2, -3]])  # Example state matrix
b = np.array([0, 1])              # Input vector

# Initial condition
x0 = np.array([1, 0])             # Example initial state

# Time vector
t = np.linspace(0, 10, 100)       # Time from 0 to 10 seconds

# Simulate the system
x = odeint(linear_system, x0, t, args=(A, b))

# Plot the results
plt.plot(t, x[:, 0], label='x1(t)')
plt.plot(t, x[:, 1], label='x2(t)')
plt.xlabel('Time [s]')
plt.ylabel('States')
plt.title('Continuous-time Linear System Simulation')
plt.legend()
plt.grid()
plt.show()
