import tensorflow as tf

# Create a scalar constant tensor
constant = tf.constant(1.0)

# Use tf.broadcast_to to fill a tensor with the scalar constant
result = tf.broadcast_to(constant, [5])

print(result) # Output: [1.0, 1.0, 1.0, 1.0, 1.0]
