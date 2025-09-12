import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Define the transfer function of the system
num = [1]
den = [1, 2, 1]

# Create a continuous-time system object
sys = signal.TransferFunction(num, den)

# Create a time vector
t = np.linspace(0, 10, 1000)

# Generate the step response
y, t = signal.step(sys, t)

# Plot the step response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid()
plt.show()
