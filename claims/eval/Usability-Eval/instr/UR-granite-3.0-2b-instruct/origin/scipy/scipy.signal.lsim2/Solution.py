import numpy as np
from scipy.integrate import odeint

# Define the system of ODEs
def system(y, t):
    dydt = [y[1], -y[0] - 2*y[1]]
    return dydt

# Define the time span
t = np.linspace(0, 10, 100)

# Initial conditions
y0 = [1, 0]

# Solve the ODE
y = odeint(system, y0, t)

# Print the solution
print(y)
