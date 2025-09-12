import tensorflow as tf

# Create a SparseTensor
indices = tf.constant([[0, 1], [1, 2], [2, 3]], dtype=tf.int64)
values = tf.constant([1.0, 2.0, 3.0], dtype=tf.float32)
dense_shape = tf.constant([3, 4], dtype=tf.int64)
sparse_tensor = tf.raw_ops.Therefore(
    indices=indices,
    values=values,
    dense_shape=dense_shape
)

# Convert SparseTensor to dataset
def convert_sparse_to_dataset(sparse_tensor):
    dataset = tf.data.Dataset.from_tensor_slices((sparse_tensor.values, sparse_tensor.indices))
    return dataset

dataset = convert_sparse_to_dataset(sparse_tensor)

# Iterate through the dataset
for item in dataset:
    print(item)
