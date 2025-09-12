import tensorflow as tf
from tensorflow import raw_ops

# Define the shapes of the input tensors
dense_tensor = [[1, 2], [3, 4]]
sparse_tensor = [5, 6]

# Create a list of sparse and dense tensors
input_tensors = [dense_tensor, sparse_tensor]

# Generate the sparse cross product using tf.raw_ops
output_tensor = raw_ops.SparseCross(inputs=input_tensors)

print("Output tensor shape:", output_tensor.shape)
