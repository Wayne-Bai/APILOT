scss
import numpy as np
from scipy.signal import cont2discrete, lsim
import matplotlib.pyplot as plt

# Define the continuous-time system
A = [[1, -0.8], [1, 2]]
B = [[1], [0]]
C = [[1]]
D = [[1]]
sys = cont2discrete((A, B, C, D), 0)

# Generate a step input and compute the output
T = np.linspace(0, 10, 1000)
u = np.zeros_like(T)
u[0] = 1
y = lsim(sys, u, T)

# Plot the step response
plt.plot(T, y[:, 0])
plt.xlabel('Time')
plt.ylabel('Output')
plt.show()
