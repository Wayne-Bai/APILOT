import tensorflow as tf

# Let's create a sample SparseTensor
indices = tf.constant([[0, 0], [1, 2], [2, 0]])
values = tf.constant([1, 2, 3])
shape = tf.constant([3, 3])

sparse_tensor = tf.SparseTensor(indices, values, shape)

# Define the number of split tensors
num_split = 2

# Split the SparseTensor along dimension 0 (default axis 0)
split_sparse_tensor = tf.sparse.split(sparse_tensor, num_split)

for i, tensor in enumerate(split_sparse_tensor):
    print(f'Unique Tensor {i}:')
    print(tensor)
    print()

# If you want to split along a specific dimension
sparse_tensor = tf.SparseTensor(indices, values, shape)
split_sparse_tensor_dim_1 = tf.sparse.split(sparse_tensor, num_split, axis=1)
print('Split along dimension 1:')
for i, tensor in enumerate(split_sparse_tensor_dim_1):
    print(f'Unique Tensor {i}:')
    print(tensor)
    print()

# Also note that split() has some optional arguments, like
#  num_or_size_splits - specifies the way to split the sparse tensor.
#  num_split = 2 means the original sparse_tensor will be split into 2 sparse tensors,
#           num_split = [1, 2] or [1, 2, 3] means the original sparse tensor will be split into
#           the specified number of  sparse tensors.
#  axis (optional) - specifies the dimension value are split along.
