# Import the necessary libraries
import tensorflow as tf
import numpy as np

# Create a 1D input tensor with shape [2, 4]
input_tensor = tf.random.normal([2, 4])

# Perform a 1D real-valued fast Fourier transform using tf.signal.rfft
output_fft = tf.signal.rfft(input_tensor,fft_length=4)

# Print the output to verify the correct result
print("Input Tensor: ", input_tensor)
print("Output FFT (Real-valued fast Fourier transform): ", output_fft)
