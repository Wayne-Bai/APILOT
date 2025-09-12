import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], dtype=tf.float32)

# Perform a real-valued fast Fourier transform
fft_result = tf.raw_ops.RealFastFourierTransform(input=input_tensor)

# Print the result
print(fft_result)
