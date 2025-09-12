import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the system coefficients
# For example, a system defined by: s^2 + 3s + 2
numerator_coeffs = [1]
denominator_coeffs = [1, 3, 2]

# Define the system using the coefficients
system = signal.TransferFunction(numerator_coeffs, denominator_coeffs)

# Compute the impulse response
t, response = signal.impulse(system)

# Plot the impulse response
plt.figure()
plt.plot(t, response)
plt.title('Impulse Response of the System')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
