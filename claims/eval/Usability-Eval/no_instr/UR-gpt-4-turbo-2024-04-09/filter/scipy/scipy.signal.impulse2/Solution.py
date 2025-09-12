import numpy as np
from scipy.signal import lti, impulse
import matplotlib.pyplot as plt

# Define system using numerator and denominator of the transfer function
numerator = [2]  # Coefficients of the numerator polynomial of the transfer function
denominator = [1, 2, 1]  # Coefficients of the denominator polynomial of the transfer function

# Create a Linear Time-Invariant system
system = lti(numerator, denominator)

# Time values for which the response is to be computed
t = np.linspace(0, 10, 500)

# Calculate the impulse response
t_out, response = impulse(system, T=t)

# Plotting the impulse response
plt.figure()
plt.plot(t_out, response)
plt.title('Impulse Response of the LTI System')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
