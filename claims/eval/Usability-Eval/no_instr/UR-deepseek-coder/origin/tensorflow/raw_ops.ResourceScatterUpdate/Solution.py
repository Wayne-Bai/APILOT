import tensorflow as tf

def assign_sparse_updates(resource, indices, updates):
    # Create a scatter update operation
    with tf.control_dependencies([tf.scatter_nd_update(resource, indices, updates)]):
        return tf.identity(resource)

# Example usage:
# Define a variable and some updates
variable = tf.Variable([0, 0, 0, 0], dtype=tf.int32)
indices = tf.constant([[1], [3]])
updates = tf.constant([9, 8])

# Apply the sparse updates
updated_variable = assign_sparse_updates(variable, indices, updates)

# Initialize the variable
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(updated_variable))  # Output: [0 9 0 8]
