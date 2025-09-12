import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Define the transfer function
num = [1]  # numerator coefficients
den = [1, 2, 1]  # denominator coefficients

# Get the impulse response
t, ir = signal.impulse((num, den))

# Plot the impulse response
plt.plot(t, ir)
plt.title('Impulse response')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
