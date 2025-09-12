import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the system: dx/dt = Ax
def linear_system(x, t, A):
    # x: state vector
    # t: time
    # A: system matrix
    return A @ x

# Define the system matrix A
A = np.array([[0.0, 1.0],
              [-2.0, -3.0]])

# Initial condition
x0 = np.array([1.0, 0.0])

# Time points where the solution is computed
t = np.linspace(0, 10, 100)

# Simulating the system
x = odeint(linear_system, x0, t, args=(A,))

# Plot results
plt.figure()
plt.plot(t, x[:, 0], label='x1(t)')
plt.plot(t, x[:, 1], label='x2(t)')
plt.xlabel('Time [s]')
plt.ylabel('Response')
plt.title('Response of a linear system')
plt.legend()
plt.grid(True)
plt.show()
