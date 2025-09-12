import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the system parameters
t = np.linspace(0, 10, 500)
sys = signal.lti([1], [1, 2, 2])

# Compute the impulse response
t, y = signal.impulse(sys, T=t)

# Plot the impulse response
plt.plot(t, y)
plt.title('Impulse Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
