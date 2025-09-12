
import tensorflow as tf

def encode_ragged_tensor(values, lengths):
    # Create a RaggedTensor from the values and lengths
    ragged_tensor = tf.RaggedTensor.from_row_lengths(values, lengths)
    
    # Encode the RaggedTensor into a variant Tensor
    variant_tensor = tf.raw_ops.EncodeRaggedTensor(input=ragged_tensor)
    
    return variant_tensor
