import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Define the system using numerator and denominator polynomials of the transfer function
numerator = [1]    # Coefficients of the numerator polynomial
denominator = [1, 3, 2]  # Coefficients of the denominator polynomial

# Create an LTI system object
system = lti(numerator, denominator)

# Compute the step response
t, y = step(system)

# Plot the step response
plt.figure()
plt.plot(t, y)
plt.title('Step Response of Continuous-Time System')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
