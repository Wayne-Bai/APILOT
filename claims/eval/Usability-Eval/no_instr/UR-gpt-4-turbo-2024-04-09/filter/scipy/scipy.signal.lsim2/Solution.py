import numpy as np
from scipy.integrate import odeint

# Define the system dynamics
def system_dynamics(x, t, a, u):
    dxdt = -a * x + u
    return dxdt

# Parameters
a = 1.0  # System parameter
u = 0.5  # Input to the system

# Initial condition
x0 = 0.0

# Time points at which the solution should be computed
t = np.linspace(0, 10, 100)  # From t=0 to t=10, 100 points

# Solve ODE
x = odeint(system_dynamics, x0, t, args=(a, u))

# Output simulation results
import matplotlib.pyplot as plt

plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('X(t)')
plt.title('Output of the Continuous-Time Linear System')
plt.show()
