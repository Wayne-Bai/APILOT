import tensorflow as tf

def ragged_to_sparse(ragged_tensor):
    # Convert RaggedTensor to SparseTensor
    sparse_tensor = tf.raw_ops.RaggedToSpdense(ragged_tensor)
    return sparse_tensor
