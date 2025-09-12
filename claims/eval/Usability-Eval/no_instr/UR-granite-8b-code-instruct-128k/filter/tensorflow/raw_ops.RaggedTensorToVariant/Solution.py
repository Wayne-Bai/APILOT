import tensorflow as tf

def ragged_tensor_to_variant(ragged_tensor):
    return tf.raw_ops.RaggedTensorToVariant(input=ragged_tensor)
