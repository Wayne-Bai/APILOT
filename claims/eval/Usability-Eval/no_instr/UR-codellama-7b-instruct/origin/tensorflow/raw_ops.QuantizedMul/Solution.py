
import tensorflow as tf

# Generate input tensors for x and y
x = tf.constant([1, 2, 3], dtype=tf.int8)
y = tf.constant([4, 5, 6], dtype=tf.int8)

# Calculate element-wise multiplication using the tf.raw_ops module
multiplication = tf.raw_ops.Mul(x=x, y=y)

# Print the output of the multiplication
print(multiplication)
