import tensorflow as tf

# Define the resource
resource = tf.config.experimental.GLOBAL_CACHE[tf.config.experimental.get_memory_usage("TFM")]

# Define the variable
variable = tf.Variable(tf.zeros([10, 10]))

# Define the updates
updates = {
    tf.raw_op.Assign(resource, tf.zeros([10, 10])): tf.constant(1.0),
    tf.raw_op.Assign(resource, tf.zeros([10, 10])): tf.constant(2.0),
    tf.raw_op.Assign(resource, tf.zeros([10, 10])): tf.constant(3.0),
}

# Apply the updates
for op, value in updates.items():
    op.apply(resource)
