import numpy as np
from scipy import signal

# Define the system transfer function
# For example, let's use a simple first-order system:
# G(s) = 1 / (s * (s + 1))
s = np.linspace(-10, 10, 1000)  # Create a complex frequency vector
G = 1 / (s * (s + 1))  # Define the transfer function

# Calculate the impulse response
t = np.linspace(0, 10, 1000)  # Create a time vector
y = signal.impulse(G, t)  # Calculate the impulse response

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response')
plt.grid()
plt.show()
