import tensorflow as tf

# Define a resource variable
resource = tf.Variable([1.0, 2.0, 3.0, 4.0, 5.0], dtype=tf.float32)

# Define indices and values for sparse updates
indices = tf.constant([0, 2, 4])
values = tf.constant([10.0, 20.0, 30.0])

# Assign sparse updates to the resource variable
update = tf.IndexedSlices(values, indices)
resource.scatter_update(update)
