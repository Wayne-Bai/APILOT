import numpy as np
from scipy.integrate import odeint

# Define the system of ODEs
def system(y, t, a, b):
    x1, x2 = y
    dx1dt = a * x1 + b * x2
    dx2dt = -a * x2
    return [dx1dt, dx2dt]

# Initial conditions
y0 = [1, 0]

# Time points
t = np.linspace(0, 10, 1000)

# Parameters
a = 2
b = 1

# Solve the ODEs
sol = odeint(system, y0, t, args=(a, b))

# Print the solution
print(sol)
