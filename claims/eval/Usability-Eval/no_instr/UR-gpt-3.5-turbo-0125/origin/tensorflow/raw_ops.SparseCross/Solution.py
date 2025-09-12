
import tensorflow as tf

# Example usage of tf.raw_ops.sparse_cross
dense_tensor = tf.constant([[1, 2], [3, 4]])
sparse_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 1]], values=[5, 6], dense_shape=[2, 2])

sparse_cross_result = tf.raw_ops.SparseCross(sparse_tensors=[sparse_tensor] + [dense_tensor])

print(sparse_cross_result)
