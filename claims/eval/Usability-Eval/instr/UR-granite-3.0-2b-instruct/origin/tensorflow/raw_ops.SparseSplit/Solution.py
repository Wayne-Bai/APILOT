import tensorflow as tf

# Define the input SparseTensor
sparse_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Define the number of split tensors
num_split = 3

# Split the SparseTensor along the first dimension
split_tensors = tf.raw_ops.Split(sparse_tensor, num_split, 0)

# Print the split tensors
for i, tensor in enumerate(split_tensors):
    print(f"Tensor {i+1}: {tensor.numpy()}")
