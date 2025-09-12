import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Define the system parameters
numerator = [1]  # Coefficients of the numerator
denominator = [1, 3, 2]  # Coefficients of the denominator

# Create a continuous-time LTI system
system = lti(numerator, denominator)

# Generate step response data
t, response = step(system)

# Plot the step response
plt.figure()
plt.plot(t, response)
plt.title('Step Response of Continuous-Time System')
plt.xlabel('Time [s]')
plt.ylabel('Response')
plt.grid()
plt.show()
