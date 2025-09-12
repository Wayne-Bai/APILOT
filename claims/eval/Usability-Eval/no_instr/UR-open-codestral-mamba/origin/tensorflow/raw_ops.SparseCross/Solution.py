import tensorflow as tf

# Step 1: Generate sparse tensors
sparse_tensor1 = tf.SparseTensor(indices=[[0, 0], [1, 2], [2, 3]],
                                 values=[1, 2, 3],
                                 dense_shape=[3, 4])
sparse_tensor2 = tf.SparseTensor(indices=[[0, 1], [1, 3], [2, 0]],
                                 values=[4, 5, 6],
                                 dense_shape=[3, 4])

# Step 2: Generate dense tensor
dense_tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
                           dtype=tf.int32)

# Step 3: Use tf.raw_ops.SparseCross
sparse_cross = tf.raw_ops.SparseCross(
    a_indices=sparse_tensor1.indices,
    a_values=sparse_tensor1.values,
    a_shape=sparse_tensor1.dense_shape,
    b_indices=sparse_tensor2.indices,
    b_values=sparse_tensor2.values,
    b_shape=sparse_tensor2.dense_shape,
    Tout_type=tf.int32,
    combiner="concat"
)
