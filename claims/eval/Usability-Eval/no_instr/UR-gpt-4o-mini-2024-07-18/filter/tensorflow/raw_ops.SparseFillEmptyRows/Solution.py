import tensorflow as tf

def fill_empty_rows(sparse_tensor, default_value):
    # Get the shape of the original sparse tensor
    shape = sparse_tensor.dense_shape
    
    # Create a dense representation of the sparse tensor
    dense_tensor = tf.sparse.to_dense(sparse_tensor, default_value=default_value)
    
    # Fill empty rows with the default value
    filled_tensor = tf.where(tf.reduce_sum(dense_tensor, axis=1, keepdims=True) == 0, 
                             tf.fill((1, shape[1]), default_value), 
                             dense_tensor)
    
    return filled_tensor

# Example usage
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

default_value = -1
result = fill_empty_rows(sparse_tensor, default_value)

print(result)
