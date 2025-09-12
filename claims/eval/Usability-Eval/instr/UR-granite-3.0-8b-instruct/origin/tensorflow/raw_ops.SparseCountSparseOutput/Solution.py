import tensorflow as tf

# Assuming you have a sparse tensor `sparse_input`
# Replace `sparse_input` with your actual sparse tensor
sparse_input = tf.SparseTensor(...)

# Define the number of bins
num_bins = 10

# Perform sparse-output bin counting
bin_counts = tf.raw_ops.SparseBinCount(
  sparse_input=sparse_input,
  num_bins=num_bins
)

# Print the bin counts
print(bin_counts)
