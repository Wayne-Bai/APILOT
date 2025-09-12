import tensorflow as tf

def fill_empty_rows(sparse_tensor, default_value):
    # Convert the SparseTensor to a dense tensor
    dense_tensor = tf.sparse.to_dense(sparse_tensor, default_value=default_value)
    
    # Convert the dense tensor back to a SparseTensor
    new_sparse_tensor = tf.sparse.from_dense(dense_tensor)
    
    return new_sparse_tensor

# Example usage:
# Create a SparseTensor
indices = tf.constant([[0, 0], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1, 2, 3], dtype=tf.int32)
dense_shape = tf.constant([3, 4], dtype=tf.int64)
sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Define the default value
default_value = tf.constant(0, dtype=tf.int32)

# Fill empty rows with the default value
filled_sparse_tensor = fill_empty_rows(sparse_tensor, default_value)

# Print the result
print(filled_sparse_tensor)
