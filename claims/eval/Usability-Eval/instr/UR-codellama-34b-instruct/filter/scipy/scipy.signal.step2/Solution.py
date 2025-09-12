import numpy as np
from scipy.signal import lti, step_response

# Define the system parameters
A = np.array([[1., 2.], [3., 4.]])
B = np.array([[5., 6.], [7., 8.]])
C = np.array([[9., 10.], [11., 12.]])
D = np.array([[13., 14.], [15., 16.]])
sys = lti(A, B, C, D)

# Generate the step response
t = np.linspace(0, 10, 1000)
u = np.zeros_like(t)
u[t > 5] = 1
x, _ = step_response(sys, u)

# Plot the results
import matplotlib.pyplot as plt
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Output')
plt.show()
