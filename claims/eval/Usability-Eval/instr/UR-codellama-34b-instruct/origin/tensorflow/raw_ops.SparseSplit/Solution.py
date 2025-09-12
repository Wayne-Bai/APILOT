
import tensorflow as tf

# Define the input sparse tensor
input_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1], [2, 2]], values=[3, 4, 5], dense_shape=[3, 3])

# Split the input tensor into multiple tensors along dimension 1
num_splits = 3
split_tensors = tf.raw_ops.sparse_split(input_tensor=input_tensor, num_splits=num_splits, axis=1)

print(split_tensors)
