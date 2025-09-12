import tensorflow as tf

# Create a SparseTensor
sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2], [2, 3], [2, 4]],
    values=[1, 2, 3, 4],
    dense_shape=[3, 5]
)

# Use tf.raw_ops_sparse_tensor_to_dense to convert sparse tensor to dense
dense_tensor = tf.raw_ops.SparseToDense(sparse_indices=sparse_tensor.indices, 
                                        sparse_values=sparse_tensor.values, 
                                        default_value=0, 
                                        output_shape=sparse_tensor.dense_shape)

# Creates a dataset that splits a SparseTensor into elements row-wise
def sparse_tensor_to_dataset(sparse_tensor):
    # Convert sparse tensor to dense tensor for easier manipulation
    dense_tensor = tf.raw_ops.SparseToDense(sparse_indices=sparse_tensor.indices, 
                                            sparse_values=sparse_tensor.values, 
                                            default_value=0, 
                                            output_shape=sparse_tensor.dense_shape)
    
    # Create dataset from dense tensor
    dataset = tf.data.Dataset.from_tensor_slices(dense_tensor)
    
    return dataset

# Example usage
dataset = sparse_tensor_to_dataset(sparse_tensor)

# Print elements of the dataset
for element in dataset:
    print(element)
