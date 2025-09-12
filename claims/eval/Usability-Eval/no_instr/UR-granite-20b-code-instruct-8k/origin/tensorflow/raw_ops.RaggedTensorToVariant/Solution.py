import tensorflow as tf

def encode_ragged_tensor(ragged_tensor):
  return tf.raw_ops.RaggedTensorToVariant(ragged_tensor=ragged_tensor)
