import numpy as np
from scipy import integrate

# Define a linear system
def linear_system(y, t):
    a = 1.0
    b = -0.5
    return np.array([y[0] + a * y[1], -y[0] * y[1] + b])

# Time span
t_span = (0, 2)
# Initial value
y0 = [1.0, 0.0]
# Solve using ODE solver
sol = integrate.odeint(linear_system, y0, t_span, tvec=np.linspace(t_span[0], t_span[1], 100))

# plot the results
import matplotlib.pyplot as plt

plt.plot(sol[:, 0], label = 'x')
plt.plot(sol[:, 1], label = 'y')
plt.xlabel('Time')
plt.ylabel('State')
plt.legend()
plt.show()
