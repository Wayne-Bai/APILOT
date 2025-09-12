import tensorflow as tf

# Example sparse updates using tf.scatter_update
def sparse_update_example(variable, indices, updates):
    tf.scatter_update(variable, indices, updates)
    return variable

# Create a mutable variable
variable = tf.Variable(tf.zeros([10]), dtype=tf.float32)

# Indices to update
indices = tf.constant([1, 3, 5])

# Updates to apply
updates = tf.constant([10.0, 20.0, 30.0])

# Performing the sparse update
updated_variable = sparse_update_example(variable, indices, updates)

# Displaying the updated variable
print(updated_variable.numpy())
