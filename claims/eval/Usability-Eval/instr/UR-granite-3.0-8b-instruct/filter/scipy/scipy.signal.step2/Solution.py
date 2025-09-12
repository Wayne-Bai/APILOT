import scipy.signal as sp
import numpy as np
import matplotlib.pyplot as plt

# Define the system transfer function
num = [1]  # Numerator coefficients
den = [1, 1]  # Denominator coefficients
sys = sp.lti(num, den)

# Generate the step response
t, y = sp.step(sys)

# Plot the step response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid()
plt.show()
