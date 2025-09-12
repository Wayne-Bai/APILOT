import tensorflow as tf

# Define the SparseTensor
indices = tf.constant([[0, 0], [1, 2], [3, 0]])
values = tf.constant([1, 2, 3])
dense_shape = tf.constant([4, 4])
sptensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Create a dataset that splits the SparseTensor row-wise
ds = tf.data.Dataset.from_tensor_slices(sptensor.values)

# Iterate over the dataset
for element in ds:
    print(element.numpy())
