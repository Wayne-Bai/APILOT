import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lti, step2

# System's transfer function coefficients
num = [1]  # Numerator coefficients (b in the transfer function)
den = [1, 1]  # Denominator coefficients (a in the transfer function)

# Create a continuous-time system
sys = lti(num, den)

# Calculate the step response
t, y = step2(sys)

# Plot the results
plt.plot(t, y)
plt.grid(True)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step Response of Continuous-Time System')
plt.show()
