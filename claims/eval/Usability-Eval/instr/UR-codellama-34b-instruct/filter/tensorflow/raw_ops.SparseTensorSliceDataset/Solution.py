
import tensorflow as tf

# Create a sparse tensor from a dense tensor
sparse_tensor = tf.convert_to_tensor(tf.ones((3, 4), dtype=tf.bool))

# Create a dataset from the sparse tensor
dataset = tf.raw_ops.SparseToDense(sparse_tensor, shape=[2, 2], default_value=0)
