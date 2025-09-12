import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 1.0, 1.0, 1.0])

# Define the FFT operation
fft_op = tf.raw_ops.FFT(input=input_tensor, direction='REAL', N=4)

# Compute the inverse FFT
ifft_op = tf.raw_ops.IFFT(input=fft_op, direction='REAL', N=4)

# Print the result
print(ifft_op)
