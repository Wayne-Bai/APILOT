import tensorflow as tf
import numpy as np

# Create a sample complex-valued input tensor
input_data = np.array([1.0 + 1j, 2.0 + 2j, 3.0 + 3j, 4.0 + 4j])
input_tensor = tf.constant(input_data, dtype=tf.complex64)

# Perform Fast Fourier Transform
fft_result = tf.signal.fft(input_tensor, inverted=True)
