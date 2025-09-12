import numpy as np
from scipy.signal import lti, step, impulse

# Define the system transfer function
num = [1]  # numerator coefficients
den = [1, 2, 1]  # denominator coefficients
sys = lti(num, den)

# Calculate the impulse response
t, y = impulse(sys, T=np.linspace(0, 10, 1000))

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.title('Impulse Response')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
