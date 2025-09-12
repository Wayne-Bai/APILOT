import tensorflow as tf

# Assuming 'var' is your variable and 'indices' is your index tensor
var = tf.Variable([1, 2, 3, 4, 5, 6])
indices = tf.constant([0, 2, 4])

# Use tf.raw_ops.Gather to gather slices
gathered_slices = tf.raw_ops.Gather(params=var, indices=indices)

# Print the gathered slices
print(gathered_slices)
