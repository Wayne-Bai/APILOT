import tensorflow as tf

# Initialize a constant tensor with a specific value
constant_tensor = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)

# Initialize a constant tensor with zeros
zeros_tensor = tf.zeros([2, 3])

# Initialize a random tensor with ones
ones_tensor = tf.ones([2, 2])

# Initialize a tenser with a range of values
range_tensor = tf.range(start=1, limit=5, delta=1)

print("Constant tensor:", constant_tensor)
print("Zeros tensor:", zeros_tensor)
print("Ones tensor:", ones_tensor)
print("Range tensor:", range_tensor)
