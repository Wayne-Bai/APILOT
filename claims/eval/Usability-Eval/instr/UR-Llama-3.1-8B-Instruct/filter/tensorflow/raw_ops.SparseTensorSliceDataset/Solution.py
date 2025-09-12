# Import required libraries
import tensorflow as tf

# Create a SparseTensor
sparse_tensor = tf.SparseTensor(
    indices=[[0, 0], [1, 0], [2, 0], [1, 1]],
    values=[1, 2, 3, 4],
    dense_shape=[3, 2]
)

# Split SparseTensor into elements row-wise
def split_sparse_tensor(sparse_tensor):
    # Reshape the SparseTensor into a SparseTensor with new shape [None, dense_shape[-1]]
    reshaped = tf.sparse.reshape(sparse_tensor, [sparse_tensor.dense_shape[0], -1])
    
    # Split the SparseTensor into row-wise elements
    split_sparse_tensor = tf.sparse.split(reshaped, sparse_tensor.dense_shape[0], axis=0)
    
    return split_sparse_tensor

split_sparse = split_sparse_tensor(sparse_tensor)

# Print the split SparseTensor
for i, sparse in enumerate(split_sparse):
    tf.print(f"Sparse Tensor at row {i}:")
    tf.print(sparse)
