import tensorflow as tf

# Assuming the variable `var` is a resource or a tensor one wants to update sparsely
# Create a variable
var = tf.Variable([5.0, 10.0, 15.0, 20.0], dtype=tf.float32)

# Sparse updates to apply - only updating indices 1 and 3
indices = tf.constant([1, 3], dtype=tf.int32)
updates = tf.constant([2.0, 4.0], dtype=tf.float32)

# Use the tf.IndexedSlices to represent sparse updates
sparse_updates = tf.IndexedSlices(values=updates, indices=indices)

# Define the division method for sparse updates
def sparse_div(resource, indices, updates):
    values = tf.gather(resource, indices)
    new_values = values / updates
    resource.assign(tf.tensor_scatter_nd_update(resource, tf.expand_dims(indices, 1), new_values))

# Applying the sparse division updates
sparse_div(var, indices, updates)

# Display the updated value of the variable
print(var.numpy())
