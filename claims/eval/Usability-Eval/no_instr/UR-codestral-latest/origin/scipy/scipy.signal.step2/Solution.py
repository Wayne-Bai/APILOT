from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

# Let's define the system
num = [1]  # Numerator coefficients
den = [1, 1]  # Denominator coefficients
sys = signal.TransferFunction(num, den)

# Compute the step response of the system
t, y = signal.step(sys)

# Plot the response
plt.figure()
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Step response of the continuous-time system')
plt.grid()
plt.show()
