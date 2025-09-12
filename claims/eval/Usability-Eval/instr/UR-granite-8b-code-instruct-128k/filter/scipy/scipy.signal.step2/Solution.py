
import scipy.signal as signal
import matplotlib.pyplot as plt
import numpy as np

# Define the system's transfer function
num = [1]  # Numerator coefficients
den = [1, 8]  # Denominator coefficients

# Generate the time vector
t = np.linspace(0, 10, 1000)

# Calculate the system's output
y, t = signal.step(num, den, t)

# Plot the step response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.title('Step Response')
plt.show()

