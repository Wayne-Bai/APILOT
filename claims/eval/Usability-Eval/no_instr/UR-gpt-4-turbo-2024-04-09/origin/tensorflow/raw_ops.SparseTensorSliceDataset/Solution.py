import tensorflow as tf

def dataset_from_sparse_tensor(sparse_tensor):
    # Using tf.data.Dataset.from_tensor_slices to create a dataset from a SparseTensor
    # by first converting the SparseTensor into a dense tensor
    dense_tensor = tf.sparse.to_dense(sparse_tensor)
    return tf.data.Dataset.from_tensor_slices(dense_tensor)

# Example usage
sparse_tensor_example = tf.SparseTensor(
    indices=[[0, 0], [1, 2]],
    values=[1, 2],
    dense_shape=[3, 4]
)

dataset = dataset_from_sparse_tensor(sparse_tensor_example)
for element in dataset:
    print(element.numpy())
