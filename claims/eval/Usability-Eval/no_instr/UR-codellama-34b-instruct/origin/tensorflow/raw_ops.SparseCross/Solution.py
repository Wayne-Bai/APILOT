import tensorflow as tf

# Create some sample data
sparse_tensor1 = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1.0, 2.0], dense_shape=[3, 4])
sparse_tensor2 = tf.SparseTensor(indices=[[1, 2], [2, 0]], values=[3.0, 4.0], dense_shape=[3, 4])
dense_tensor = tf.constant([[5, 6, 7, 8]])

# Use the SparseCross operation to generate sparse crosses
sparse_cross = tf.raw_ops.SparseCross(
    a=sparse_tensor1, b=sparse_tensor2, c=dense_tensor, hash_key=tf.string)

# Print the resulting sparse cross tensor
print(sparse_cross.to_dense())
