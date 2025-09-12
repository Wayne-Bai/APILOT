
import tensorflow as tf

def encode_ragged_tensor(ragged_tensor):
    variant_tensor = tf.raw_ops.EncodeRaggedTensor(ragged_values=ragged_tensor.values, nested_splits=ragged_tensor.row_splits)
    return variant_tensor
