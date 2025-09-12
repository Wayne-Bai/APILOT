import tensorflow as tf

# Initialize some sparse tensors for example
indices1 = [[0, 0], [1, 2]]
values1 = [1, 2]
shape1 = [2, 3]
sparse1 = tf.SparseTensor(indices=indices1, values=values1, dense_shape=shape1)

indices2 = [[0, 0], [1, 1]]
values2 = [3, 4]
shape2 = [2, 3]
sparse2 = tf.SparseTensor(indices=indices2, values=values2, dense_shape=shape2)

# Initialize a dense tensor for example
dense = tf.constant([[5, 6, 7], [8, 9, 10]], dtype=tf.float32)

# Create a SparseCross object
sparse_cross = tf.raw_ops.SparseCross(sp_indices=[sparse1.indices, sparse2.indices],
                                        sp_values=[sparse1.values, sparse2.values],
                                        sp_shape=shape1,
                                        dense_inputs=[dense],
                                        hash_key=12345)

# Run the computation
with tf.Session() as sess:
    result = sess.run(sparse_cross)
