import tensorflow as tf

# Define the variable and resource
variable = tf.Variable(tf.random.normal([3, 3]))
resource = tf.resource_variable_v2(variable)

# Define the sparse updates
sparse_updates = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)

# Divide the sparse updates into the resource
resource.scatter_add(tf.sparse.from_dense(sparse_updates), [0, 1])
