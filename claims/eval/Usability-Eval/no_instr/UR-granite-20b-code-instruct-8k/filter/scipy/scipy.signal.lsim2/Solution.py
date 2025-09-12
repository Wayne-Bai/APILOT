import numpy as np
from scipy.integrate import odeint

# Define the system of differential equations
def sys_ode(x, t, a, b):
    dxdt = [a*x[0] - b*x[1], a*x[1] + b*x[0]]
    return dxdt

# Define the parameters for the system
a = 2.5
b = 1.5

# Define the initial conditions
x0 = [1, 0]

# Define the time points for the simulation
t = np.linspace(0, 10, 100)

# Solve the system of differential equations
x = odeint(sys_ode, x0, t, args=(a, b))

# Print the output of the system
print(x)
