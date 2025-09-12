
import tensorflow as tf

# Define input sparse and dense tensors
sparse_tensors = [tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1.0, 2.0], dense_shape=[2, 3])]
dense_tensors = [tf.constant([[3.0, 4.0, 5.0], [6.0, 7.0, 8.0]])]

# Generate sparse cross from the input tensors
sparse_cross = tf.raw_ops.SparseCrossed(sparse_tensors=sparse_tensors, dense_tensors=dense_tensors)

# Print the generated sparse cross tensor
print(sparse_cross)
