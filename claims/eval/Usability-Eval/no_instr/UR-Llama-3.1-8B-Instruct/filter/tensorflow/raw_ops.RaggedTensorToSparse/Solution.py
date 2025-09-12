import tensorflow as tf

# Create a RaggedTensor
rt_values = [[1, 2, 3], [4], [5, 6]]
rt_row_splits = [0, 2, 3, 4]
rt = tf.RaggedTensor.from_row_splits(values=rt_values, row_splits=rt_row_splits)

# Convert the RaggedTensor to a SparseTensor
st_indices = tf.constant(tf.where(rt.values!= 0).numpy(), dtype=tf.int64)
st_values = tf.gather(rt.values, tf.where(rt.values!= 0))
st_shape = tf.shape(rt.values)

sp_t = tf.SparseTensor(indices=st_indices, values=st_values, dtype=tf.float32, shape=st_shape)

# Convert the SparseTensor to a numpy array
sp_t = tf.sparse.reorder(sp_t)
numpy_sparse_t = sp_t.numpy()

print(numpy_sparse_t)
