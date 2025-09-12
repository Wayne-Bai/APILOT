# Import required libraries
import tensorflow as tf
import numpy as np

# Function to perform component-wise division of a SparseTensor by a dense Tensor
def sparse_tensor_div(sparse_values, sparse_indices, dense_tensor):
    # Create a SparseTensor
    sparse_tensor = tf.SparseTensor(indices=sparse_indices, values=sparse_values, dense_shape=[3, 3])
    
    # Perform component-wise division
    result_sparse_tensor = tf.raw_ops.SparseTensorDenseMatMul(
        a=sparse_tensor,
        b=tf.linalg.inv(dense_tensor),
        adjoint_b=False,
        adjoint_a=False
    )
    
    return result_sparse_tensor

# Test the function
if __name__ == "__main__":
    sparse_values = np.array([1, 2, 3], dtype=np.float32)
    sparse_indices = np.array([[0, 0], [1, 2], [0, 1]], dtype=np.int64)
    dense_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 10]], dtype=tf.float32)
    
    result_sparse_tensor = sparse_tensor_div(sparse_values, sparse_indices, dense_tensor)
    print(result_sparse_tensor)
