import tensorflow as tf

# Create a real-valued input tensor
real_input = tf.constant([1.0, 2.0, 3.0, 4.0], dtype=tf.float32)

# Compute the real-valued fast Fourier transform using tf.signal.rfft
fft_result = tf.signal.rfft(real_input)

# Print the result
print("Real-valued FFT Result:", fft_result.numpy())
