import tensorflow as tf

# Define the input 2D SparseTensor
indices = [[0, 0], [1, 2]]
values = [1, 2]
dense_shape = [3, 4]
input_sparse_tensor = tf.sparse.SparseTensor(indices, values, dense_shape)

# Convert the SparseTensor to a dense Tensor
dense_tensor = tf.sparse.to_dense(input_sparse_tensor, default_value=0)

# Fill empty rows with a default value
filled_dense_tensor = tf.where(tf.equal(dense_tensor, 0), tf.constant(99), dense_tensor)

print(filled_dense_tensor)
