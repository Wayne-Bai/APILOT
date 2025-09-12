import tensorflow as tf

# Create a tensor of real numbers
real_numbers = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0], dtype=tf.float32)

# Perform real-valued fast Fourier transform
fft_result = tf.signal.rfft(real_numbers)

# Print the result
print(fft_result)
