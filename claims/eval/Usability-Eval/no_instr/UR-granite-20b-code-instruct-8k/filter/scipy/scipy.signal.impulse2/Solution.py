import scipy.signal

# Define the system transfer function
num = [1]
den = [1, 2, 1]
sys = scipy.signal.TransferFunction(num, den)

# Calculate the impulse response
t, y = scipy.signal.impulse(sys)

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, y)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Impulse Response')
plt.show()
