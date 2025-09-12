
import numpy as np
from scipy.integrate import odeint

# Define the continuous-time linear system
def system(y, t):
    return -2*y + 3*np.sin(t)

# Set initial condition
y0 = 1

# Define time points
t = np.linspace(0, 10, 100)

# Solve the ODE using odeint
solution = odeint(system, y0, t)

print(solution)
