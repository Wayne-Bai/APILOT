
# Importing the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Defining the system's transfer function
numerator = [1]
denominator = [1, 1, 1]  # Example transfer function: 1 / (s^2 + s + 1)
system = signal.TransferFunction(numerator, denominator)

# Generating the step response of the continuous-time system
time, response = signal.step(system)

# Plotting the step response
plt.plot(time, response)
plt.xlabel('Time')
plt.ylabel('Response')
plt.title('Step Response of Continuous-Time System')
plt.grid()
plt.show()
