import tensorflow as tf

def sparse_tensor_divide_by_dense(sparse_tensor, dense_tensor):
    # Ensure the shapes are compatible for broadcasting
    sparse_tensor_shape = tf.shape(sparse_tensor)
    dense_tensor_shape = tf.shape(dense_tensor)
    broadcast_shape = tf.broadcast_dynamic_shape(sparse_tensor_shape, dense_tensor_shape)

    # Broadcast the dense tensor to match the shape of the sparse tensor
    dense_tensor = tf.reshape(dense_tensor, broadcast_shape)

    # Perform element-wise division
    result = tf.raw_ops.SparseTensorDenseDivide(sparse_tensor, dense_tensor)

    return result
