import tensorflow as tf

# Assuming x and y are quantized buffers
# You can replace the quantized buffers with your actual data
x = tf.raw_ops.QuantizedBuffer(tensor=tf.constant([1, 2, 3, 4]), min_value=0, max_value=15, narrow_range=False)
y = tf.raw_ops.QuantizedBuffer(tensor=tf.constant([5, 6, 7, 8]), min_value=0, max_value=15, narrow_range=False)

# Perform element-wise multiplication
result = tf.raw_ops.QuantizedMul(x, y)

# Print the result
print(result)
