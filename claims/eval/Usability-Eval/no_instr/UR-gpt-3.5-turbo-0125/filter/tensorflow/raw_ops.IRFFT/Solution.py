
import tensorflow as tf

# Define the input tensor
input_tensor = tf.constant([[1.0, 2.0], [3.0, 4.0]])

# Apply the Inverse real-valued fast Fourier transform
output = tf.raw_ops.Irfft(input_tensor)

print(output)
