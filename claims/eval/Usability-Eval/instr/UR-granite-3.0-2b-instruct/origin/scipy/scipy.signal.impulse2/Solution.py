import numpy as np
from scipy import signal

# Define the system transfer function
s = np.symbols('s')  # Laplace variable
G = 1 / (s**2 + 2*s + 1)  # Example system transfer function

# Define the input signal
t = np.linspace(0, 10, 1000)  # Time vector from 0 to 10 seconds with 1000 points
u = np.zeros_like(t)  # Zero input signal
u[500] = 1  # Impulse at t = 5 seconds

# Compute the impulse response
y, _ = signal.impulse(G, u, t)

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response of the System')
plt.grid()
plt.show()
