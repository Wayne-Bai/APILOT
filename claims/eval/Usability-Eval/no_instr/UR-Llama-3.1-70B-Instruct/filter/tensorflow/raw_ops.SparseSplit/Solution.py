import tensorflow as tf

# Sample sparse tensor
sparsetensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2], [3, 4], [4, 1]],
                                      values=[1, 2, 3, 4],
                                      dense_shape=[5, 5])

# Split the sparse tensor into 2 parts along the first dimension (axis=0)
num_split = 2
split_sparse_tensor, split_info = tf.raw_ops.Split(
    input=sparsetensor,
    num_split=num_split,
    axis=0
)

# Print the results
with tf.Session() as sess:
    sess.run(tf.tables_initializer())
    split_sparse_tensor_values = sess.run(split_sparse_tensor)
    split_info_values = sess.run(split_info)

    print("Split Sparse Tensor Values:")
    for i, split_sparse_tensor_value in enumerate(split_sparse_tensor_values):
        print("Split {}".format(i))
        print("Indices:", split_sparse_tensor_value.indices)
        print("Values:", split_sparse_tensor_value.values)
        print("Dense Shape:", split_sparse_tensor_value.dense_shape)
        print()

    print("Split Info:", split_info_values)
