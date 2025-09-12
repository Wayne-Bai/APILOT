import tensorflow as tf

def generate_sparse_cross(sparse_tensors, dense_tensors):
    # Create a list to hold the sparse tensors
    sparse_inputs = []
    
    # Add sparse tensors to the input list
    for sparse_tensor in sparse_tensors:
        sparse_inputs.append(sparse_tensor)

    # Add dense tensors to the input list
    for dense_tensor in dense_tensors:
        sparse_inputs.append(tf.expand_dims(dense_tensor, axis=0))

    # Generate the sparse cross
    sparse_cross = tf.experimental.numpy.concatenate(sparse_inputs, axis=0)

    return sparse_cross

# Example usage:
# Define some sparse and dense tensors
sparse_tensor_1 = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
sparse_tensor_2 = tf.sparse.SparseTensor(indices=[[0, 1]], values=[3], dense_shape=[2, 3])

dense_tensor_1 = tf.constant([[1, 2], [3, 4]])
dense_tensor_2 = tf.constant([[5], [6]])

# Call the function with sparse and dense tensors
result = generate_sparse_cross([sparse_tensor_1, sparse_tensor_2], [dense_tensor_1, dense_tensor_2])
print(result)
