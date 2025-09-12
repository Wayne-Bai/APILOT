import tensorflow as tf
import numpy as np

# Create a sample input
input_tensor = tf.constant([3.0, 4.0, 1.0, 2.0], dtype=tf.float32)
input_tensor = tf.reshape(input_tensor, shape=[1, 2, 2])

# Apply the real-valued fast Fourier transform
fft_result = tf.raw_ops.RealFFT(input_tensor)

# Print the result
print("Original Input:")
print(input_tensor)
print("\nReal FFT Output:")
print(fft_result)

# Create a complex-valued output
complex_output = tf.complex(real=fft_result[0], imag=fft_result[1])

# Print the complex-valued output
print("\nComplex FFT Output:")
print(complex_output)

# To validate the output with numpy
input_array = np.array([3.0, 4.0, 1.0, 2.0])
input_array = np.reshape(input_array, newshape=(1, 2, 2))
# numpy FFT of the array
numpy_fft = np.fft.rfftn(input_array, axes=[1, 2])
print("\nNumpy FFT Output:")
print(numpy_fft)
