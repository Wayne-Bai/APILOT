import tensorflow as tf

# Let's start with a real-valued Tensor
real_values = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)

# Calculate the Fast Fourier Transform (FFT)
fft_result = tf.signal.fft(real_values)

# Print the result
print(fft_result)
