import tensorflow as tf

# Define the resource
resource = tf.VariableResource(tf.resource("Resource:0"))

# Define the updates
updates = {resource: tf.constant([1.0, 2.0, 3.0])}

# Create the operation
assign_op = tf.raw_ops.Assign(resource, updates)

# Execute the operation
with tf.Session() as sess:
    sess.run(assign_op)
