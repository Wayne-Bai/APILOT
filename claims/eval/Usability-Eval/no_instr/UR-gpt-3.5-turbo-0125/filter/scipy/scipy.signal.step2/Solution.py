
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Define the system parameters
numerator = [1]
denominator = [1, 1, 1]

# Create a transfer function
sys = signal.TransferFunction(numerator, denominator)

# Calculate the step response
t, y = signal.step(sys)

# Plot the step response
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step Response of Continuous-time System')
plt.grid()
plt.show()
