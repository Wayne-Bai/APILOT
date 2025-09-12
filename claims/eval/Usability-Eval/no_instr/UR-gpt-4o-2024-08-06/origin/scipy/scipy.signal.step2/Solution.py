import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the system: Numerator and Denominator coefficients of the transfer function
numerator = [1]      # Example: G(s) = 1 / (s^2 + 2s + 1)
denominator = [1, 2, 1]

# Create a transfer function system
system = signal.TransferFunction(numerator, denominator)

# Compute the step response
t, y = signal.step(system)

# Plot the step response
plt.figure()
plt.plot(t, y)
plt.title('Step Response')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
