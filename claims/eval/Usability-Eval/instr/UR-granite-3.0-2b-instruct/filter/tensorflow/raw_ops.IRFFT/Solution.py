import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([-1.0, 0.0, 1.0], dtype=tf.float32)

# Define the FFT operation
fft_operation = tf.raw_ops.InverseRealValuedFFT, input_tensor

# Perform the FFT operation
output_tensor = tf.raw_ops.InverseRealValuedFFT(input_tensor)

# Print the output tensor
print(output_tensor)
