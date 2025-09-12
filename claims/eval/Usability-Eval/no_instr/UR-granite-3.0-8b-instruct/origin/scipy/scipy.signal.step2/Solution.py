import numpy as np
import scipy.signal as signal

# Define the system transfer function
num = [1]  # Numerator coefficients
den = [1, 2, 1]  # Denominator coefficients
sys = signal.TransferFunction(num, den)

# Define the input signal
t = np.linspace(0, 10, 1000)  # Time vector
u = np.unit_impulse(100)  # Unit impulse function

# Compute the step response
t, y, x = signal.step2(sys, T=t, X0=0, U=u)

# Plot the step response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.title('Step Response')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
