import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the input data
x = np.linspace(0, 10, 1000)

# Define the frequency response of the filter (a uniform filter in this case)
freq = np.array([0.2, 0.3, 0.4, 0.5])

# Create a Kaiser filter based on the frequency response
b, a = signal.kaiserord(61, np.max(freq))

# Design the filter
w, h = signal.kaiser(b, a, fs=1000)

# Apply the filter to the input signal
y = signal.lfilter(h, 1, x)

# Plot the results
plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.plot(x, label='Input signal')
plt.plot(y, label='Filtered signal')
plt.legend()

plt.subplot(122)
plt.plot(np.abs(signal.freqz(h)))
plt.xlabel('Frequency (normalised)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
