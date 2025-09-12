import tensorflow as tf

# Define the input tensors
x = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.int32)
y = tf.constant([[7, 8, 9], [10, 11, 12]], dtype=tf.int32)

# Calculate the element-wise product of x and y
xy_product = tf.raw_ops.Mul(x=x, y=y)

print(xy_product)
