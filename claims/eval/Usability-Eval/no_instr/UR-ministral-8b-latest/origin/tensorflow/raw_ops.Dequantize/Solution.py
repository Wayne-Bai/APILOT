import tensorflow as tf

# Define a method to dequantize the input tensor
def dequantize(tensor):
    return tf.raw_ops.DequeueData(tensor=tensor.name)

# Create a sample input tensor
input_tensor = tf.constant(10, shape=(1,), dtype=tf.uint8)

# Dequantize the input tensor
dequantized_tensor = dequantize(input_tensor)
print(dequantized_tensor)
