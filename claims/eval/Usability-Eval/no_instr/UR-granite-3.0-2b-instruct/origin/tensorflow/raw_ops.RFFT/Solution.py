import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])

# Define the FFT operation using tf.raw_ops
fft_op = tf.raw_ops.FFT(input=input_tensor, direction='N', input_size=6, batch_size=1, output_type=tf.complex64)

# Execute the FFT operation
fft_result = fft_op.execute()

# Print the result
print(fft_result)
