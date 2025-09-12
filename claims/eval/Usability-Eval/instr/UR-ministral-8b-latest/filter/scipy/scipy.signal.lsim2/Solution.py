import numpy as np
from scipy.integrate import odeint

# Define the system dynamics
def system_dynamics(y, t, A):
    return np.dot(A, y)

# Parameters of the system
A = np.array([[1.0, -0.5],
              [0.3,  1.2]])

# Initial conditions
y0 = np.array([1.0, 0.0])

# Time span
t = np.linspace(0, 10, 400)

# Solve the ODE
sol = odeint(system_dynamics, y0, t, args=(A,))

# Plot the result
import matplotlib.pyplot as plt

plt.figure()
plt.plot(t, sol)
plt.xlabel('Time [s]')
plt.ylabel('Output')
plt.title('Simulation of a Continuous-Time Linear System')
plt.grid(True)
plt.show()
