import scipy.signal as signal
import matplotlib.pyplot as plt

# Define the system's transfer function
def transfer_function(omega):
    return 1 / (1 + omega**2)

# Define the time vector
t = np.linspace(0, 10, 1000)

# Calculate the output response
y = signal.step(transfer_function, t)

# Plot the output response
plt.plot(t, y)
plt.xlabel('Time (s)')
plt.ylabel('Output')
plt.show()
