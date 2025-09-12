import tensorflow as tf

# Create a SparseTensor
sparse_tensor = tf.sparse.SparseTensor(
    indices=[[0, 0], [1, 2], [2, 3]],
    values=[3, 4, 5],
    dense_shape=[5, 6]
)

# Split the SparseTensor along a given dimension
# Here, let's say we want to split along 0th dimension (rows) into 2 parts
num_split = 2
axis = 0

# Splitting the SparseTensor
split_sparse_tensors = tf.sparse.split(axis, num_split, sparse_tensor)

# To evaluate and print the result, we can use the following
for i, split_tensor in enumerate(split_sparse_tensors):
    print(f"Split {i}:")
    print(tf.sparse.to_dense(split_tensor))
