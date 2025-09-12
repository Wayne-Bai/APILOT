import numpy as np
from scipy import signal

# Define the system transfer function
# For example, let's use a simple 2nd order system
num = [1]  # Numerator coefficients
den = [1, 2, 1]  # Denominator coefficients

# Generate time points
t = np.linspace(0, 10, 1000)

# Compute impulse response
t, y = signal.impulse((num, den), T=t)

# Plot impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Impulse Response')
plt.grid()
plt.show()
