import tensorflow as tf

def encode_ragged_tensor_to_variant(rt):
    return tf.raw_ops.RaggedTensorToVariant(input_rt=rt)
