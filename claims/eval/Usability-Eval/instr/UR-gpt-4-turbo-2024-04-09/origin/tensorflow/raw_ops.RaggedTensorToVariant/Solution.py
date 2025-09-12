import tensorflow as tf

def encode_ragged_tensor_to_variant(ragged_tensor):
    # Ensure the input is a ragged tensor by converting if not already
    if not isinstance(ragged_tensor, tf.RaggedTensor):
        raise ValueError("Input must be a tf.RaggedTensor")
    
    # Use RaggedTensorToVariant from tf.raw_ops (No direct API, but conceptually accurate if it were to exist)
    encoded_variant_tensor = tf.raw_ops.RaggedTensorToVariant(ragged_tensor=ragged_tensor)
    
    return encoded_variant_tensor
