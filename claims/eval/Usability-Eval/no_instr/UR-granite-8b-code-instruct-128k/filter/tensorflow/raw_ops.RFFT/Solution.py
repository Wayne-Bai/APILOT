import tensorflow as tf

# Define the input signal
signal = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)

# Perform the real-valued fast Fourier transform
fft = tf.raw_ops. FFT(signal)

# Print the result
print(fft)
