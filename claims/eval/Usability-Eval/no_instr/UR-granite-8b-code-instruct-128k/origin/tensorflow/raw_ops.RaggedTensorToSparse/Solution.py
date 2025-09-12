import tensorflow as tf

def convert_ragged_to_sparse(ragged_tensor):
    return tf.raw_ops.RaggedTensorToSparse(ragged_tensor=ragged_tensor)
