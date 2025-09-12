# Importing the necessary modules
import tensorflow as tf

# Code to encode a RaggedTensor into a variant Tensor
def encode_ragged_tensor(ragged_tensor):
    """
    Encodes a RaggedTensor into a variant Tensor.

    Args:
    ragged_tensor: A TensorFlow RaggedTensor.

    Returns:
    A variant Tensor containing the encoded RaggedTensor.
    """
    encoded_tensor = tf.raw_ops.EncodeRaggedTensor(
        row_splits=ragged_tensor.row_splits, 
        value=ragged_tensor.values
    )
    
    return tf.reshape(encoded_tensor, [-1])


# Example usage
ragged_tensor = tf.RaggedTensor.from_row_splits(
    values=[1, 2, 3, 4, 5, 6, 7, 8],
    row_splits=[0, 2, 4, 6, 9]
)

encoded_tensor = encode_ragged_tensor(ragged_tensor)

print(encoded_tensor)
