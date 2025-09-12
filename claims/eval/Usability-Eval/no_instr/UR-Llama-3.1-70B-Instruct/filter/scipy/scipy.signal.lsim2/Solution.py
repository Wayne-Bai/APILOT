import numpy as np
from scipy.integrate import odeint

# Define the system dynamics
def system_dynamics(state, t):
    """
    This function defines the dynamics of a continuous-time linear system.
    
    Parameters:
    state (numpy array): State vector of the system.
    t (float): Time.
    
    Returns:
    numpy array: Derivative of the state vector.
    """
    A = np.array([[1, 2], [3, -4]])  # System matrix
    B = np.array([[5], [6]])  # Input matrix
    u = np.sin(t)  # Input signal
    dxdt = np.dot(A, state) + np.dot(B, np.array([u]))
    return dxdt

# Initial condition
x0 = np.array([1, 0.5])

# Time points
t = np.linspace(0, 10, 100)

# Solve ODE
solution = odeint(system_dynamics, x0, t)

# Print solution
import matplotlib.pyplot as plt
plt.plot(t, solution[:, 0], label='State 1')
plt.plot(t, solution[:, 1], label='State 2')
plt.xlabel('Time')
plt.ylabel('States')
plt.title('States over time')
plt.legend()
plt.grid()
plt.show()
