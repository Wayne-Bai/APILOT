import numpy as np
from scipy.integrate import odeint

# Define the system of differential equations
def system(state, t, A, B):
    x, y = state
    dxdt = A[0, 0] * x + A[0, 1] * y + B[0]
    dydt = A[1, 0] * x + A[1, 1] * y + B[1]
    return [dxdt, dydt]

# Define the initial conditions
x0 = [1, 0]

# Define the time span
t = np.linspace(0, 10, 1000)

# Define the system matrix A and input matrix B
A = np.array([[1, 2], [3, 4]])
B = np.array([5, 6])

# Solve the system of differential equations
states = odeint(system, x0, t, args=(A, B))

# Print the solution
for state in states:
    print(state)
