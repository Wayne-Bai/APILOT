import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Define the continuous-time system
numerator = [1]  # Example: numerator coefficients of the transfer function
denominator = [1, 1]  # Example: denominator coefficients of the transfer function
system = lti(numerator, denominator)

# Compute the step response
t, y = step(system)

# Plot the step response
plt.plot(t, y)
plt.title('Step Response of Continuous-Time System')
plt.xlabel('Time [s]')
plt.ylabel('Output')
plt.grid()
plt.show()
