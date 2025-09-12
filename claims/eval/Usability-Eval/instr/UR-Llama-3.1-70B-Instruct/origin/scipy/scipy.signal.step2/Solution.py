import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Define the transfer function numerator and denominator polynomials
num = [1]  # numerator polynomial
den = [1, 2, 1]  # denominator polynomial

# Define the time points
t = np.linspace(0, 10, 1000)

# Compute the step response
y = signal.lti(num, den).step(T=t)[1]

# Plot the step response
plt.plot(t, y)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.title('Step Response of Continuous-Time System')
plt.grid(True)
plt.show()
