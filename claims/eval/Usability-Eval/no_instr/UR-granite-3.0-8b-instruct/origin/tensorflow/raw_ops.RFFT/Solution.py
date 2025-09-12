import tensorflow as tf

# Define the input signal
signal = tf.linspace(0.0, 1.0, 1000)

# Compute the fast Fourier transform
fft_result = tf.signal.rfft(signal)

# Compute the magnitude of the FFT result
magnitude = tf.abs(fft_result)

# Compute the frequency axis
frequency_axis = tf.range(fft_result.shape[0], dtype=tf.float32) * (1.0 / (signal.shape[0] / 2.0))

# Print the magnitude and frequency axis
print("Magnitude:", magnitude.numpy())
print("Frequency Axis:", frequency_axis.numpy())
