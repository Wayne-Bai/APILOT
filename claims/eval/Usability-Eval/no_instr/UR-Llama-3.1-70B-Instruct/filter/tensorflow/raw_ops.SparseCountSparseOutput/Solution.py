import tensorflow as tf

# Create a sparse tensor
sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2], [2, 3], [4, 1]],
    values=[1.0, 2.0, 3.0, 4.0],
    dense_shape=[5, 4]
)

# Define the operator to perform sparse-output bin counting
bin_count = tf.raw_ops.SparseBincount(
    sparse_indices=sparse_tensor.indices,
    sparse_values=sparse_tensor.values,
    sparse_shape=sparse_tensor.dense_shape,
    bin_size=2.0,
    dtype=tf.float32
)

# Create a session to run the operation
with tf.Session() as sess:
    # Run the operation
    result = sess.run(bin_count)
    
    # Print the result
    print(result)
