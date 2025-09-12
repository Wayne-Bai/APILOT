import tensorflow as tf

# Assuming this is your original input
x = tf.constant([[0, 1, 2], [3, 4], [5, 6, 7]])

# Assuming this is your index tensor
indices = tf.constant([[1, 1, 2, 0], 1, 2, 1])

# Use tf.raw_ops to gather a specific subarray from the original input tensor
gathered = tf.raw_ops.GatherSlices(x=x, params=indices, axis=0)

print(gathered)
