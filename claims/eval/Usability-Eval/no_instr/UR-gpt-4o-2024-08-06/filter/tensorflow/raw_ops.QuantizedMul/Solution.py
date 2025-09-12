import tensorflow as tf

# Create two quantized tensors
x = tf.constant([1, 2, 3, 4], dtype=tf.qint8)  # Example quantized tensor with qint8 type
y = tf.constant([5, 6, 7, 8], dtype=tf.qint8)  # Another example quantized tensor with qint8 type

# Cast the quantized tensors to a common type suitable for multiplication
x_cast = tf.cast(x, tf.int32)
y_cast = tf.cast(y, tf.int32)

# Element-wise multiplication
result = tf.multiply(x_cast, y_cast)

# Convert the result back to qint8 if needed (loses precision)
# Here, it is cast back to qint8 for demonstration but caution: it may cause overflow
result_quantized = tf.cast(result, tf.qint8)

print(result_quantized.numpy())
