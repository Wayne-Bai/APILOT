import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], dtype=tf.float32)

# Perform the real-valued fast Fourier transform
fft_result = tf.raw_ops.FFT(input=input_tensor, input_dtype=tf.float32, output_dtype=tf.complex64)

# Print the result
print(fft_result)
