import tensorflow as tf

# Assume 'resource' is a tensor variable.
resource = tf.Variable([1, 2, 3, 4, 5])

# Define the indices to gather.
indices = tf.constant([0, 2, 4], dtype=tf.int32)

# Use tf.raw_ops.GatherV2 to gather slices from the variable according to indices.
result = tf.raw_ops.GatherV2(resource_handle=resourcehandle, params=resource, indices=indices)

# Initialize a session and run the operation to see the result.
with tf.compat.v1.Session() as sess:
    sess.run(tf.compat.v1.global_variables_initializer())
    gathered_values = sess.run(result)

print(gathered_values)
