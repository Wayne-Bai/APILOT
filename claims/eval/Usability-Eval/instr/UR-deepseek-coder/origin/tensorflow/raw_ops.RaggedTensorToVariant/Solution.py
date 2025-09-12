import tensorflow as tf

def ragged_tensor_to_variant(ragged_tensor):
    # Convert RaggedTensor to a dense tensor
    dense_tensor = ragged_tensor.to_tensor()
    
    # Encode the dense tensor into a variant tensor
    variant_tensor = tf.raw_ops.EncodeTensor(tensor=dense_tensor)
    
    return variant_tensor

# Example usage:
# ragged_tensor = tf.ragged.constant([[1, 2], [3]])
# variant_tensor = ragged_tensor_to_variant(ragged_tensor)
