
import numpy as np
from scipy import signal

# Define the transfer function of the system
def tf(s):
    return s + 1

# Compute the impulse response of the system using the transfer function
impulse_response = signal.impulse(tf, N=100)

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(impulse_response)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Impulse Response of a Single-Input Continuous-Time Linear System')
plt.show()
