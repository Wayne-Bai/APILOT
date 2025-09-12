import scipy.integrate as spi

def sys(x, t):
    # Define the system of ODEs
    dxdt = [x[1], -x[0] - 2*x[1]]
    return dxdt

# Initial conditions
x0 = [1, 0]

# Time span
t = [0, 10]

# Solve the ODE system
sol = spi.odeint(sys, x0, t)

# Print the solution
print(sol)
