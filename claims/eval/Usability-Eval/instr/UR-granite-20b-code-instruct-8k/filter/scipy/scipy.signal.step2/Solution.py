import scipy.signal as sig
import numpy as np

# Define the system transfer function
num = [1]
den = [1, 1]
sys = sig.TransferFunction(num, den)

# Generate the step response
t, y = sig.step(sys)

# Plot the step response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Step Response')
plt.grid()
plt.show()
