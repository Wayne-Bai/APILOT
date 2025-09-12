import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define system coefficients (example system: second-order system)
numerator = [1.0]  # Coefficients of the transfer function numerator
denominator = [1.0, 2.0, 2.0]  # Coefficients of the transfer function denominator

# Create a transfer function system
system = signal.TransferFunction(numerator, denominator)

# Generate the impulse response
t, response = signal.impulse(system)

# Plot the results
plt.figure()
plt.plot(t, response)
plt.title('Impulse Response of the System')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
