import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the system parameters
numerator_coeffs = [1.0]  # Coefficients of the numerator of the transfer function
denominator_coeffs = [1.0, 2.0, 2.0]  # Coefficients of the denominator of the transfer function

# Create a continuous-time linear system
system = signal.TransferFunction(numerator_coeffs, denominator_coeffs)

# Calculate the impulse response
t, y = signal.impulse(system)

# Plot the impulse response
plt.figure()
plt.plot(t, y)
plt.title("Impulse Response of the System")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
