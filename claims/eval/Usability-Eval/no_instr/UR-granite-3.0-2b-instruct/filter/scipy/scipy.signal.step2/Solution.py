import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the transfer function of the system
s = np.fft.fftfreq(len(t), 1/Ts)
H = 1 / (s**2 + 2*s + 1)

# Create time vector
t = np.linspace(0, 10, len(t))

# Create step response
y = signal.step(t, T=Ts)

# Plot the step response
plt.plot(t, y)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
