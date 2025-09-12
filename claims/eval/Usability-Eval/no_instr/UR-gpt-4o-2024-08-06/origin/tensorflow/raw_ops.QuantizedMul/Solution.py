import tensorflow as tf

# Define the quantized input tensors
# Typically, quantized tensors are of dtype tf.quint8, tf.qint8, etc.
x = tf.constant([1, 2, 3], dtype=tf.quint8)
y = tf.constant([4, 5, 6], dtype=tf.quint8)

# Cast the quantized tensors to float for operations
x_float = tf.cast(x, tf.float32)
y_float = tf.cast(y, tf.float32)

# Perform the element-wise multiplication
result = tf.multiply(x_float, y_float)

# Cast the result back to quantized type, if necessary
# Here we assume a preference to keep results in float
print("Result:", result.numpy())
