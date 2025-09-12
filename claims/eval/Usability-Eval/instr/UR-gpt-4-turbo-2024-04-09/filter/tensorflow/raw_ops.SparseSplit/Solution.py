import tensorflow as tf

def split_sparse_tensor(sparse_tensor, num_splits, axis):
    # Split the SparseTensor into `num_splits` along the specified `axis`
    return tf.sparse.split(sp_input=sparse_tensor, num_split=num_splits, axis=axis)

# Example usage
# Create a SparseTensor
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]

sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Specify the number of splits and the axis along which to split
num_splits = 2
axis = 1

# Split the SparseTensor
split_tensors = split_sparse_tensor(sparse_tensor, num_splits, axis)

# Print the outputs
for i, split_tensor in enumerate(split_tensors):
    print(f"SparseTensor {i}:")
    print("Indices:", split_tensor.indices.numpy())
    print("Values:", split_tensor.values.numpy())
    print("Dense Shape:", split_tensor.dense_shape.numpy())
