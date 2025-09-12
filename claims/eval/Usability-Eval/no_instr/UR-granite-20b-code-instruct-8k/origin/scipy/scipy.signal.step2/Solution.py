import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define system transfer function
num = [1]
den = [1, 5]
sys = signal.TransferFunction(num, den)

# Generate step response
t, y = signal.step(sys)

# Plot step response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid()
plt.show()
