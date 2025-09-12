import tensorflow as tf

# Function to create and encode a RaggedTensor
def encode_ragged_tensor():
    # Create a RaggedTensor
    ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

    # Encode RaggedTensor into a variant Tensor using 'tf.ragged.to_variant()'
    variant_tensor = tf.ragged.to_variant(ragged_tensor)

    return variant_tensor

# Example usage
encoded_tensor = encode_ragged_tensor()
print(encoded_tensor)
