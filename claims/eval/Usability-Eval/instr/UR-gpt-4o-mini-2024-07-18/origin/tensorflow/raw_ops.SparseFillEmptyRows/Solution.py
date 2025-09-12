import tensorflow as tf

def fill_empty_rows(sparse_tensor, default_value):
    # Ensure the input is a SparseTensor
    if not isinstance(sparse_tensor, tf.sparse.SparseTensor):
        raise ValueError("Input must be a SparseTensor.")
    
    # Get the dense shape of the SparseTensor
    dense_shape = sparse_tensor.dense_shape
    
    # Create a dense representation of the SparseTensor
    dense_tensor = tf.sparse.to_dense(sparse_tensor, default_value=default_value)
    
    # Fill the empty rows with the specified default value
    filled_tensor = tf.where(tf.equal(dense_tensor, 0), default_value, dense_tensor)
    
    # Convert the filled tensor back to SparseTensor format
    filled_sparse_tensor = tf.sparse.from_dense(filled_tensor)
    
    return filled_sparse_tensor

# Example Usage
# Create a SparseTensor
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]
sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

default_value = 0
filled_sparse_tensor = fill_empty_rows(sparse_tensor, default_value)

# To print the result
print(tf.sparse.to_dense(filled_sparse_tensor))
