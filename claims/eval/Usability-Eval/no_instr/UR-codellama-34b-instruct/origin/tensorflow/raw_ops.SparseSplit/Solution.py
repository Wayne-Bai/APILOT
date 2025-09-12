
import tensorflow as tf

# Create a SparseTensor with some values
sparse_tensor = tf.SparseTensor(indices=[[0, 1], [1, 2], [2, 3]], values=[1, 2, 3])

# Split the SparseTensor into two tensors along dimension 1
tensors = tf.raw_ops.split(sparse_tensor, axis=1)
