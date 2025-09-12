# Importing necessary TensorFlow modules
import tensorflow as tf

# Creating a sample RaggedTensor
rt = tf.ragged.constant([[1, 2, 3], [4], [5, 6, 7, 8]])

# Converting the RaggedTensor into a SparseTensor
st = tf.sparse.RaggedTensorToSparse(rt)

# Printing the SparseTensor
print(st)

# Converting the SparseTensor into a RaggedTensor using tf.sparse.to_ragged_sparse
rtd = tf.sparse.to_ragged_sparse(st)

# Printing the Stubbed RaggedTensor
print(rtd.to_list())
