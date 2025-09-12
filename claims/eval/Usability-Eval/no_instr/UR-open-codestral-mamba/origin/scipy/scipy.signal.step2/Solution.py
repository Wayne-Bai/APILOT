# Import necessary libraries
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt

# Define system characteristics
numerator = [1]  # Numerator of transfer function
denominator = [1, 3, 2]  # Denominator of transfer function

# Create the transfer function object
sys = signal.TransferFunction(numerator, denominator)

# Define time array
t = np.linspace(0, 5, 500)

# Define step input
step_input = np.zeros_like(t)
step_input[t >= 0] = 1.0

# Compute step response
tout, yout, xout = signal.lsim(sys, step_input, t)

# Plot step response
plt.figure()
plt.plot(tout, yout)
plt.title('Step response of transfer function')
plt.xlabel('time')
plt.ylabel('value')
plt.show()
