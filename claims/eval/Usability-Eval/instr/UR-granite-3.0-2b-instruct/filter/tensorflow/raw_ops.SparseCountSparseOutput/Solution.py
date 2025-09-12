import tensorflow as tf

# Define the sparse tensor input
sparse_tensor = tf.constant([[0, 0, 0], [1, 0, 0], [0, 2, 0], [0, 0, 3]])

# Perform sparse-output bin counting
bin_counting = tf.raw_ops.SparseToDense(
    sparse_input=sparse_tensor,
    output_type=tf.int64,
    default_value=-1,
    name="sparse_to_dense"
)

# Print the result
print(bin_counting.numpy())
