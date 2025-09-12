import tensorflow as tf

# Create a tensor
x = tf.constant([1.0, 2.0, 3.0])
y = tf.constant([4.0, 5.0, 6.0])

# Perform division using tf.raw_ops.Div
result = tf.raw_ops.Div(x, y)
