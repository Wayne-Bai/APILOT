
import tensorflow as tf

# Generate a random integer tensor of shape (2, 3)
input_tensor = tf.random.uniform((2, 3), maxval=10, dtype=tf.int32)

# Convert the integer tensor to a float or bfloat16 Tensor using Dequantize
output_tensor = tf.raw_ops.Dequantize(input=input_tensor, num_bits=8)

print("Input tensor:", input_tensor)
print("Output tensor:", output_tensor)
