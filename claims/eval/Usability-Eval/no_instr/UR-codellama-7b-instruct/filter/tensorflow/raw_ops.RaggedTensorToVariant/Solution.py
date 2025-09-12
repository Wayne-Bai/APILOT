
import tensorflow as tf

def encode_ragged_tensor(input_tensor):
    """Encode a RaggedTensor into a variant Tensor.

    Args:
        input_tensor: A `RaggedTensor`.

    Returns:
        A `VariantTensor`, representing the encoded ragged tensor.
    """
    # Create a RaggedTensor from the input
    ragged_tensor = tf.ragged.constant(input_tensor)
    
    # Convert the RaggedTensor into a VariantTensor
    variant_tensor = ragged_tensor.to_variant()
    
    return variant_tensor
