import tensorflow as tf

# Dummy data
variable_data = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
indices = tf.constant([0, 2])

# Using tf.raw_ops.Gather to gather slices
raw_gather_op = tf.raw_ops.Gather(
    params=variable_data, indices=indices, validate_indices=False)

raw_gather_output = tf.numpy_function(raw_gather_op, [], tf.int32)

print(raw_gather_output.numpy())
