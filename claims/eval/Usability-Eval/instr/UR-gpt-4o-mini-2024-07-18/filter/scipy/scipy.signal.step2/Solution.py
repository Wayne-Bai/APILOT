import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step

# Define system parameters (example: a second-order system)
numerator = [1]  # Numerator coefficients
denominator = [1, 3, 2]  # Denominator coefficients (s^2 + 3s + 2)

# Create continuous-time system
system = lti(numerator, denominator)

# Generate time points
t = np.linspace(0, 10, 500)

# Get step response
t, response = step(system, T=t)

# Plot the step response
plt.figure(figsize=(10, 6))
plt.plot(t, response)
plt.title('Step Response of Continuous-Time System')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')
plt.grid()
plt.show()
