import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the right-hand side of the system
def linear_system(state, t, A, B, U):
    """
    Define the linear system dynamics.

    Parameters:
    state (numpy array): Current state of the system.
    t (float): Time
    A (numpy array): System matrix
    B (numpy array): Input matrix
    U (float or numpy array): Input

    Returns:
    numpy array: Derivatives of the system state
    """
    # Define the dynamics of the system
    dstate_dt = np.dot(A, state) + B * U
    return dstate_dt

# System matrices
A = np.array([[-1, 1], [0, -2]])  # System matrix
B = np.array([[0], [1]])  # Input matrix

# Input
U = 1.0

# Time points
t = np.linspace(0, 10, 100)

# Initial condition
state0 = [1.0, 0.0]

# Solve ODE
state = odeint(linear_system, state0, t, args=(A, B, U))

# Plot results
plt.plot(t, state)
plt.xlabel('t')
plt.legend(['State 1', 'State 2'])
plt.grid()
plt.show()
