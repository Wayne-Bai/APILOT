import tensorflow as tf

# Create a SparseTensor
sparse_tensor = tf.sparse.from_dense(
    tf.constant([[0, 0, 0], [1, 2, 3], [4, 5, 6]]),
    default_value=0
)

# Create a dataset that splits the SparseTensor into elements row-wise
dataset = tf.data.Dataset.from_tensor_slices((sparse_tensor,))
dataset = dataset.map(lambda x: tf.sparse.to_dense(x))
dataset = dataset.batch(3)

# Print the dataset
for elements in dataset:
    print(elements)
