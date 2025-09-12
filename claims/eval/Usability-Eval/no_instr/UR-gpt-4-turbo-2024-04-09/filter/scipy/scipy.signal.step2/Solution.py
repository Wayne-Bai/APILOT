import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Define system parameters
numerator = [1] # the coefficients of the numerator of the transfer function
denominator = [1, 3, 2] # the coefficients of the denominator of the transfer function

# Create the system using the LTI (Linear Time Invariant) system class
system = lti(numerator, denominator)

# Calculate the step response
time, response = step(system)

# Plot the response
plt.plot(time, response)
plt.title('Step Response of Continuous-Time System')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
