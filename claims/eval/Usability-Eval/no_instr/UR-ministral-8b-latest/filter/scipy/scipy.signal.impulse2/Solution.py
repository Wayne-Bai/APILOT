import numpy as np
import scipy.signal as signal

# Define the system's transfer function
def transfer_function(s):
    num = [1]  # Numerator coefficients
    den = [1, 2]  # Denominator coefficients
    return signal.TransferFunction(num, den)

# Define the sampling frequency and duration of the response
fs = 1000  # Sampling frequency in Hz
T = 0.02  # Response duration

# Generate the impulse response
t = np.linspace(0, T, fs * T, endpoint=False)  # Time vector
impulse_response = signal.lsim(transfer_function, signal.Impulse(), T, (t,))

# Plot the impulse response
import matplotlib.pyplot as plt
plt.plot(t, impulse_response[0])
plt.title('Impulse Response of the System')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()
