
import numpy as np
from scipy.signal import impulse

# Define the system parameters
A = np.array([[0, 1], [0, 0]])
B = np.array([[0], [1]])
C = np.array([[1, 0]])
D = np.array([[0]])
sys = ss(A, B, C, D)

# Calculate the impulse response of the system
t, y = impulse(sys)

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Impulse Response of System')
plt.show()
