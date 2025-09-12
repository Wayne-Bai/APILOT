import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the system parameters
num = [1]  # Numerator coefficients of the transfer function
den = [1, 2, 1]  # Denominator coefficients of the transfer function

# Create a continuous-time transfer function
system = signal.TransferFunction(num, den)

# Generate the impulse response
t, response = signal.impulse(system)

# Plot the impulse response
plt.figure()
plt.plot(t, response)
plt.title('Impulse Response of the Continuous-Time Linear System')
plt.xlabel('Time [s]')
plt.ylabel('Response')
plt.grid()
plt.show()
