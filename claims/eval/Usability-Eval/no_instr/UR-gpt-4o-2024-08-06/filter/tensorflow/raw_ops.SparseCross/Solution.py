import tensorflow as tf

def generate_sparse_cross(sparse_inputs, dense_inputs):
    # Use tf.sparse.cross function to generate sparse cross
    # This will automatically handle both sparse and dense inputs.
    sparse_cross = tf.sparse.cross(sparse_inputs=sparse_inputs, dense_inputs=dense_inputs)
  
    return sparse_cross

# Example usage:

# Create some sample sparse tensors
sparse_tensor_1 = tf.sparse.SparseTensor(indices=[[0, 0], [1, 0]], values=['a', 'b'], dense_shape=[3, 1])
sparse_tensor_2 = tf.sparse.SparseTensor(indices=[[0, 0], [2, 0]], values=['c', 'd'], dense_shape=[3, 1])

# Create some sample dense tensors
dense_tensor_1 = tf.constant(['x', 'y', 'z'])

# Generate sparse cross
result = generate_sparse_cross([sparse_tensor_1, sparse_tensor_2], [dense_tensor_1])

# Use .numpy() to see the result if you are using eager execution
print("Sparse Cross Indices:\n", result.indices.numpy())
print("Sparse Cross Values:\n", result.values.numpy())
print("Sparse Cross Dense Shape:\n", result.dense_shape.numpy())
