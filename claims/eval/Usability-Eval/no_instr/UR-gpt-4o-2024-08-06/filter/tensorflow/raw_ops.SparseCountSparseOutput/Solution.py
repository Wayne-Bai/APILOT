import tensorflow as tf

# Create a sparse tensor for demonstration
indices = [[0, 0], [1, 2], [2, 3]]
values = [1, 2, 3]
dense_shape = [3, 4]
sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Define the data type for the output
output_dtype = tf.int64

# Perform sparse-output bin counting
# The `sparse_bincount` function computes the number of occurrences of each value in a sparse tensor.
# It returns a dense tensor representing counts of each value.

bincounts = tf.sparse.sparse_dense_cwise(tf.raw_ops.Bincount,
                                         input=sparse_tensor,
                                         weights=None,
                                         minlength=0,  # Minimum size of the output tensor
                                         maxlength=-1, # Maximum size of the output tensor
                                         dtype=output_dtype)

# Execute the operation and print the result
with tf.Session() as sess:
    result = sess.run(bincounts)
    print("Sparse Tensor Bin Counts:", result)
