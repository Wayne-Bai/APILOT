import tensorflow.compat.v1 as tf

# Assume inputs
indices = [[0, 0], [1, 2], [2, 3]]
values = [1, 2, 3]
dense_shape = [3, 4]

# Define sparse tensor
input_sparse_tensor = tf.SparseTensor(indices, values, dense_shape)

# Define dimension along which to split
split_dim = 1

# Define number of splits
num_split = 2

# Apply tf.raw_ops.SparseSplit
outputs = tf.compat.v1.sparse.split(input_sparse_tensor, num_split, split_dim)

# Print outputs
for i, output in enumerate(outputs):
    print(f"Output {i+1}:")
    print(f"Indices: {output.indices.numpy()}")
    print(f"Values: {output.values.numpy()}")
    print(f"Dense Shape: {output.dense_shape}")
    print("--------------------")
