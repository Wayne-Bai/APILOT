# Import necessary libraries
import tensorflow as tf
import numpy as np

# Create a random complex-valued input tensor
input_tensor = tf.complex(tf.random.uniform((1, 10)), tf.random.uniform((1, 10)))

# Perform 1D FFT on the input tensor
fft_out = tf.signal.fft(input_tensor)

# Perform inverse FFT
ifft_out = tf.raw_ops.IFFT(input=fft_out)

# Optionally, use the `signal.ifft` function, which provides a more convenient
# interface and handles the nuances of inverse FFT
ifft_out_convenient = tf.signal.ifft(input=fft_out)

# Print the inputs, FFT outputs, and inverse FFT outputs
print("Input tensor:")
print(input_tensor)

print("\nFFT output:")
print(fft_out)

print("\nInverse FFT output (using tf.raw_ops.IFFT):")
print(ifft_out)

print("\nInverse FFT output (using tf.signal.ifft):")
print(ifft_out_convenient)
