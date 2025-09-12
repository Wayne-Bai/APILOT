import tensorflow as tf

# Example SparseTensor
indices = [[0, 0], [1, 2], [2, 3]]
values = [1, 2, 3]
dense_shape = [3, 4]
sparse_tensor = tf.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)

# Split the SparseTensor along the first dimension
num_split = 3
split_tensors = tf.sparse.split(sparse_tensor, num_split, axis=0)

# To convert the split tensors back to normal tensors for display
split_dense_tensors = [tf.sparse.to_dense(s) for s in split_tensors]

# Print the result
for i, tensor in enumerate(split_dense_tensors):
    print(f"Split tensor {i}:\n{tensor.numpy()}")
