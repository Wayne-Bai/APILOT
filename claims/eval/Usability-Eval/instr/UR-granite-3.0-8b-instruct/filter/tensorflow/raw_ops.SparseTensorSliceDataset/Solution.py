import tensorflow as tf

# Assuming you have a SparseTensor named 'sparse_tensor'
# Create a dataset from the SparseTensor
dataset = tf.raw_ops.SparseTensorToRagged(sparse_tensor, row_partition_dtype=tf.string)

# Print the dataset
for element in dataset:
    print(element)
