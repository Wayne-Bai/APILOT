import tensorflow as tf

def encode_ragged_tensor(ragged_tensor):
    # Convert the RaggedTensor to a dense tensor
    dense_tensor = ragged_tensor.to_tensor()
    
    # Create a variant tensor from the dense tensor
    variant_tensor = tf.raw_ops.EncodeTensor(tensor=dense_tensor)
    
    return variant_tensor

# Example usage:
# ragged_tensor = tf.ragged.constant([[1, 2], [3]])
# encoded_variant_tensor = encode_ragged_tensor(ragged_tensor)
