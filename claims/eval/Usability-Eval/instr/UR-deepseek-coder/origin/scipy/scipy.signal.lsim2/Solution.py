import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system of ODEs
def linear_system(y, t, A):
    return np.dot(A, y)

# Define the system matrix A
A = np.array([[-1, 2], [-2, -1]])

# Initial conditions
y0 = np.array([1, 0])

# Time points
t = np.linspace(0, 10, 100)

# Solve the ODE
y = odeint(linear_system, y0, t, args=(A,))

# Plot the results
plt.plot(t, y[:, 0], label='y1')
plt.plot(t, y[:, 1], label='y2')
plt.xlabel('Time')
plt.ylabel('State')
plt.legend()
plt.show()
