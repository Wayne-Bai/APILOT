# Import necessary libraries
import tensorflow as tf

# Create a sample sparse tensor
sparse_tensor = tf.SparseTensor(
    indices=[[0, 0], [1, 0], [1, 1]],
    values=[1, 2, 3],
    dense_shape=[2, 2]
)

# Reshape the sparse tensor to (2, 2) and convert it to a dense tensor
dense_tensor = tf.sparse.to_dense(sparse_tensor)

# Reshape the dense tensor to (-1)
res_shaped_tensor = tf.reshape(dense_tensor, (-1))

# Create a dataset that splits the reshaped tensor row-wise
dataset = tf.data.Dataset.from_tensor_slices(res_shaped_tensor)

# Print the dataset
print([item for item in dataset.as_numpy_iterator()])
