
import tensorflow as tf

def create_sparse_tensor_dataset(indices, values, dense_shape):
    sparse_tensor = tf.sparse.SparseTensor(indices=indices, values=values, dense_shape=dense_shape)
    dataset = tf.data.Dataset.from_tensor_slices(sparse_tensor)
    return dataset
