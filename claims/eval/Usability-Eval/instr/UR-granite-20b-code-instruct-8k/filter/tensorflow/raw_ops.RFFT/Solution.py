import tensorflow as tf

# Define the input signal
input_signal = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)

# Compute the fast Fourier transform
fft = tf.signal.fft(input_signal)

# Print the result
print(fft)
