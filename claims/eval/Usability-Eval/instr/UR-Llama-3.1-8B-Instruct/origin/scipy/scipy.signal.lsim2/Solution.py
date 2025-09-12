import numpy as np
from scipy.integrate import odeint

# Define the model parameters
A = 1.0  # magnitude of the sine wave
omega = 1.0  # frequency of the sine wave
x0 = 1.0  # initial condition for x
y0 = 1.0  # initial condition for y

# Define the system of ordinary differential equations
def model(state, t, A, omega):
    x, y = state
    dxdt = A * np.sin(omega * t)
    dydt = -0.1 * A * np.sin(omega * t)
    return [dxdt, dydt]

# Generate an array of time points
t = np.linspace(0, 10, 101)

# Solve the system of ODEs using odeint
state0 = [x0, y0]
state = odeint(model, state0, t, args=(A, omega))

# Print the solution
print('Time (s)    x   y')
for i in range(len(t)):
    print(f'{t[i]:.2f}    {state[i, 0]:.4f}    {state[i, 1]:.4f}')

# Plot the solution (optional)
import matplotlib.pyplot as plt

plt.plot(t, state[:, 0], 'b', label='x')
plt.plot(t, state[:, 1], 'r', label='y')
plt.xlabel('t (s)')
plt.ylabel('x, y')
plt.title('Solution of the ODE system')
plt.legend(loc='best')
plt.grid()
plt.show()
