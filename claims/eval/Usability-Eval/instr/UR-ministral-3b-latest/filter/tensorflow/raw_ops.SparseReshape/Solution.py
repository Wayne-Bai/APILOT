import tensorflow as tf

# Create a SparseTensor
sparse_data = tf.SparseTensor([...], [], ...)

# Reshape the SparseTensor to a new dense shape
dense_tensor = sparse_data.to_dense()

