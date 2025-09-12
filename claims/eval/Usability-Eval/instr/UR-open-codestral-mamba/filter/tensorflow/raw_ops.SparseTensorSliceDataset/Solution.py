import tensorflow as tf

def split_sparse_tensor(sparse_tensor):
    # Convert SparseTensor to a dense tensor
    dense_tensor = tf.sparse.to_dense(sparse_tensor)

    # Transpose the dense tensor so that rows become columns
    transposed_tensor = tf.transpose(dense_tensor)

    # Split the transposed tensor into individual vectors
    split_tensor = tf.split(transposed_tensor, sparse_tensor.shape[1], axis=1)

    # Convert each vector back to a dense tensor and wrap them into a SparseTensor
    split_sparse_tensors = [tf.sparse.from_dense(tf.reshape(tensor, [sparse_tensor.shape[0], -1])) for tensor in split_tensor]

    return split_sparse_tensors
