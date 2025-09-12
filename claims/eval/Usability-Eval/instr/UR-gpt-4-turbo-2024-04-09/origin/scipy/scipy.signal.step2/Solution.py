import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Define system using numerator and denominator of the transfer function
numerator = [1]  # Coefficients of the numerator polynomial
denominator = [1, 2, 1]  # Coefficients of the denominator polynomial

# Create LTI system object
system = lti(numerator, denominator)

# Get the time values and step response of the system
t, response = step(system)

# Plotting the step response
plt.figure()
plt.plot(t, response)
plt.title('Step response of the system')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
