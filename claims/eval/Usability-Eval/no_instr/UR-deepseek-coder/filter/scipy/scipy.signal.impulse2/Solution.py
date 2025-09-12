import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the system parameters
numerator = [1]  # Numerator coefficients of the transfer function
denominator = [1, 2, 1]  # Denominator coefficients of the transfer function

# Create the transfer function
sys = signal.TransferFunction(numerator, denominator)

# Compute the impulse response
t, h = signal.impulse(sys)

# Plot the impulse response
plt.plot(t, h)
plt.title('Impulse Response')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
