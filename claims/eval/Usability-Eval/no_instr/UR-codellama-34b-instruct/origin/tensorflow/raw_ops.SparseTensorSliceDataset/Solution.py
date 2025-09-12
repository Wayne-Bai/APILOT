
import tensorflow as tf

# Create a SparseTensor with 3 rows and 2 columns
values = [1, 2, 3, 4]
indices = [[0, 0], [1, 1], [2, 2]]
dense_shape = [3, 2]
st = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Split the SparseTensor into elements row-wise using the `tf.data.experimental.sparse_tensor_dataset` API
dataset = tf.data.experimental.sparse_tensor_dataset(st)

# Print the elements of the dataset
for element in dataset:
  print(element)
