import tensorflow as tf

# Define a sparse update function
def sparse_variable_update(variable, indices, updates):
    # Create a SparseTensor from indices and updates
    sparse_tensor = tf.SparseTensor(indices=indices, values=updates, dense_shape=tf.shape(variable))

    # Apply the sparse update to the variable
    tf.raw_ops.ResourceScatterUpdate(
        resource=variable,
        updates=sparse_tensor.values,
        indices=sparse_tensor.indices
    )

# Example usage
if __name__ == "__main__":
    # Create a variable
    variable = tf.Variable(tf.zeros([3, 3]), dtype=tf.float32)

    # Define indices and updates
    indices = [[0, 1], [1, 2], [2, 0]]  # Sparse indices
    updates = [5.0, 10.0, 15.0]          # Values to update the variable with

    # Call the sparse update function
    sparse_variable_update(variable, indices, updates)

    # Print updated variable
    print(variable.numpy())
