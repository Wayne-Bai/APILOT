import tensorflow as tf

# Define the variable
variable = tf.Variable([1, 2, 3, 4, 5])

# Define the indices
indices = tf.constant([1, 3])

# Create the gather operation
gather = tf.raw_ops.ResourceGather(resource=variable, indices=indices)

# Print the result
with tf.Session() as sess:
    print(sess.run(gather))
