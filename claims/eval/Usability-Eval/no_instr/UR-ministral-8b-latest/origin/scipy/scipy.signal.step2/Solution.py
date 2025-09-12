import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Define the system transfer function
s = signal.TransferFunction([1, 1], [1, -0.5, 0.1])

# Define sampling frequency and time span
fs = 100  # Hz
t = np.linspace(0, 1, 10000)  # seconds

# Calculate the step response
_, step_response = signal.lsim(s, np.ones((1, len(t))), t)

# Plot the step response
plt.plot(t, step_response)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.grid()
plt.show()
