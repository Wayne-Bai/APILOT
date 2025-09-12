import tensorflow as tf

# Define the input SparseTensor
sparse_tensor = tf.SparseTensor(indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])

# Split the SparseTensor into 2 tensors along dimension 1
num_split = 2
split_sparse_tensors = tf.raw_ops.Split(split_dim=1, num_split=num_split, value=sparse_tensor)

# Print the resulting split SparseTensor objects
for i, split_tensor in enumerate(split_sparse_tensors):
    print(f"Split SparseTensor {i+1}:")
    print(split_tensor)
