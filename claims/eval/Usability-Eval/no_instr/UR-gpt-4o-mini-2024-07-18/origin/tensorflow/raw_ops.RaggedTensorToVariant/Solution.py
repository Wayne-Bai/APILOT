import tensorflow as tf

# Function to encode a RaggedTensor into a variant Tensor
def encode_ragged_tensor(ragged_tensor):
    # Ensure the input is a RaggedTensor
    if not isinstance(ragged_tensor, tf.RaggedTensor):
        raise ValueError("Input must be a RaggedTensor.")
    
    # Encode the RaggedTensor
    encoded_tensor = tf.raw_ops.RaggedTensorToVariant(ragged_tensor=ragged_tensor)
    return encoded_tensor

# Example usage
if __name__ == "__main__":
    # Create a RaggedTensor
    ragged_tensor = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])
    
    # Encode the RaggedTensor
    encoded = encode_ragged_tensor(ragged_tensor)
    
    print("Encoded RaggedTensor:", encoded)
