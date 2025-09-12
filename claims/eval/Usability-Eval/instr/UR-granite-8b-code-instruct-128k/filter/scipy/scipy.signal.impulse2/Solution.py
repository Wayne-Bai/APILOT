
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Define the system transfer function
def transfer_function(w):
    return 1 / (1 + w**2)

# Define the time vector
t = np.linspace(0, 10, 1000)

# Generate the impulse response
impulse_response = signal.convolve(t, transfer_function(2*np.pi*t), mode='full')

# Plot the impulse response
plt.figure()
plt.plot(t, impulse_response)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response')
plt.show()
