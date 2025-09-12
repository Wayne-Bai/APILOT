import numpy as np
from scipy.integrate import odeint

# Define the parameters of the system
A = np.array([[0, 1], [0, 0]])
B = np.array([[1, 0], [0, 1]])
C = np.array([[1, 0], [0, 1]])
D = np.zeros((2, 2))

# Define the initial conditions
x0 = np.array([0, 0])
t_span = (0, 10)
dt = 0.01

# Create a function to integrate the system
def ode(t, x):
    return A @ x + B @ u(t)

# Define the output function
def y(t):
    return C @ x(t)

# Simulate the system using odeint
x = odeint(ode, x0, t_span, args=(B, D), dt=dt)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(t_span, y(x))
plt.show()
