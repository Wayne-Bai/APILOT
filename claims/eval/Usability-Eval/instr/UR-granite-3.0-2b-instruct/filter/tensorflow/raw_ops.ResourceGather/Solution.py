import tensorflow as tf

# Create a resource variable
resource_var = tf.resource_variable(name="my_resource", shape=[10])

# Create a constant tensor
constant_tensor = tf.constant([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create indices tensor
indices = tf.constant([[0], [2], [4], [6], [8]])

# Create a Gather operation
gather_op = tf.raw_ops.Gather(
    resource=resource_var,
    indices=indices,
    axis=0,
    output_type=tf.int32
)

# Run the Gather operation
with tf.Session() as sess:
    result = sess.run(gather_op)
    print(result)
