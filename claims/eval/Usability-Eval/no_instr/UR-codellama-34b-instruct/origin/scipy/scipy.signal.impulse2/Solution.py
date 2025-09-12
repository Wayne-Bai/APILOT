import numpy as np
from scipy import signal

# Define the system transfer function
num = [1]
den = [1, 2, 3, 4]
sys = signal.TransferFunction(num, den)

# Generate the impulse response of the system
t, y = signal.impulse(sys, np.linspace(0, 10, 100))

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response of a Single-Input Continuous-Time Linear System')
plt.show()
