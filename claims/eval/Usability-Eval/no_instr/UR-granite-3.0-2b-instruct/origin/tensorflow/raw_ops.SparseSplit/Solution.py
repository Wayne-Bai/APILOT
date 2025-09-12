import tensorflow as tf

# Create a SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 1], [2, 2]], values=[1, 2, 3], dense_shape=[3, 3])

# Split the SparseTensor into 2 tensors along the first dimension
split_tensors = tf.raw_ops.SplitSparse(sparse_tensor, num_split=2, axis=0)

# Print the split tensors
print("Tensor 1:")
print(split_tensors[0])
print("Tensor 2:")
print(split_tensors[1])
