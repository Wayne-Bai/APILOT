import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the system transfer function
numerator = [1]
denominator = [1, 2, 1]  # For a system like 1 / (s^2 + 2s + 1)

# Define the time points where we want to evaluate the step response
t = np.linspace(0, 10, 100)

# Calculate the step response
t, y = signal.step((numerator, denominator), T=t)

# Plot the step response
plt.figure(figsize=(8, 6))
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response of Continuous-Time System')
plt.grid(True)
plt.show()
