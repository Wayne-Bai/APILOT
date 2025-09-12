import tensorflow as tf

def create_sparse_tensor_dataset(sparse_tensor):
    # Check if input is a SparseTensor
    if not isinstance(sparse_tensor, tf.sparse.SparseTensor):
        raise ValueError("Input must be a tf.sparse.SparseTensor")

    # Create a dataset from the SparseTensor
    dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor)

    return dataset

# Example usage
sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2]], 
    values=[1, 2], 
    dense_shape=[2, 3]
)

dataset = create_sparse_tensor_dataset(sparse_tensor)

for element in dataset:
    print(element)
