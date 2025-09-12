# Import necessary libraries
import tensorflow as tf

# Create a tensor with quantized int32 values
input_tensor = tf.constant([1, 2, 3], dtype=tf.qint32)

# Create a tensor with quantized float16 values
bias_tensor = tf.constant([0.1, 0.2, 0.3], dtype=tf.qint32)

# Apply element-wise addition of bias to input
result_tensor = tf.raw_ops.AddV2(x=input_tensor, y=bias_tensor)

# Print the result
print(result_tensor)
