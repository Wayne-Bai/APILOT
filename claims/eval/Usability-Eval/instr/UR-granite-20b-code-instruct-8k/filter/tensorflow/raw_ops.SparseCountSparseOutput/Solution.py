import tensorflow as tf

# Define the input tensor
input_tensor = tf.sparse.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Define the bin counts
bin_counts = [0, 1, 2, 3, 4]

# Perform sparse-output bin counting
output_tensor = tf.raw_ops.SparseBincount(
    input=input_tensor,
    weights=None,
    minlength=0,
    maxlength=0,
    dtype=tf.int32,
    axis=-1,
    bin_counts=bin_counts
)

# Print the output tensor
print(output_tensor)
