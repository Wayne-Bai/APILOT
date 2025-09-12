
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Compute the inverse real-valued fast Fourier transform
inverse_fft = tf.signal.irfft(input_tensor)

# Print the result
print(inverse_fft)
