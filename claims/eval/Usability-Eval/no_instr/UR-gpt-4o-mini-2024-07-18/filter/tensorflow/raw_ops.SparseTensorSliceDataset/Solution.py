import tensorflow as tf

def split_sparse_tensor(sparse_tensor):
    # Check if the input is a SparseTensor
    if not isinstance(sparse_tensor, tf.SparseTensor):
        raise ValueError("The input must be a tf.SparseTensor.")

    # Create a dataset from the SparseTensor that splits it into elements row-wise
    dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor)

    return dataset

# Example usage
indices = [[0, 0], [1, 2], [2, 1]]
values = [1, 2, 3]
dense_shape = [3, 4]

sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
dataset = split_sparse_tensor(sparse_tensor)

for element in dataset:
    print(element)
