# Import the TensorFlow library
import tensorflow as tf

# Create a SparseTensor
indices = [[0, 0], [1, 2], [2, 1]]
values = [1.0, 2.0, 3.0]
dense_shape = [3, 3]
sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Create a dense Tensor
dense_tensor = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]], dtype=tf.float32)

# Perform component-wise division
result = tf.math.divide(sparse_tensor, dense_tensor)

# Print the result
print(result)
