import tensorflow as tf

# Create sparse and dense tensors
sparse_tensor1 = tf.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=[1, 2],
    dense_shape=[3, 3]
)

sparse_tensor2 = tf.SparseTensor(
    indices=[[1, 0], [2, 0], [2, 2]],
    values=[1, 2, 3],
    dense_shape=[3, 3]
)

dense_tensor1 = tf.constant([[1, 0, 0], [0, 2, 0], [0, 0, 3]])
dense_tensor2 = tf.constant([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# Function to generate sparse cross from a list of sparse and dense tensors
def sparse_cross(tensors):
    sparse_tensors = []
    dense_tensors = []
    
    for tensor in tensors:
        if isinstance(tensor, tf.SparseTensor):
            sparse_tensors.append(tensor)
        elif isinstance(tensor, tf.Tensor):
            dense_tensors.append(tensor)
    
    cross = tf.cross(
        tf.sparse.to_dense(tf.sparse.concat(sparse_tensors, 0), name="out_of_range_0"), 
        tf.concat(dense_tensors, 0)
    )
    
    return cross

# Create a list of tensors and apply sparse_cross function
tensors = [sparse_tensor1, dense_tensor1, sparse_tensor2, dense_tensor2]
output = sparse_cross(tensors)

print(output)
