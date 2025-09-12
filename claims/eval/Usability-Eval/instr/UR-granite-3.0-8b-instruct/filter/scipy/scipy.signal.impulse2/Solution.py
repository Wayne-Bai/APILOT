import numpy as np
from scipy.signal import lti, impulse

# Define the system
# For example, let's consider a simple system with a transfer function H(s) = 1 / (s + 1)
num = [1]
den = [1, 1]
sys = lti(num, den)

# Generate the impulse response
t, y = impulse(sys, T=np.linspace(0, 10, 1000))

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.title('Impulse Response')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
