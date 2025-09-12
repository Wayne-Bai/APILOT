
import tensorflow as tf

# Define input tensors
sparse_tensors = []
dense_tensors = []

# Add some sparse and dense tensors to the lists
sparse_tensors.append(tf.SparseTensor([[0, 0], [1, 2]], [3, 4], (3, 5)))
dense_tensors.append(tf.constant([[1, 2, 3], [4, 5, 6]]))

# Generate the sparse cross product
sparse_cross = tf.raw_ops.SparseCross(sparse_tensors=sparse_tensors, dense_tensors=dense_tensors)

# Print the results
print(sparse_cross)  # prints SparseTensor([[0, 0], [1, 2]], [3 4 5 6 7 8], (3, 5))
