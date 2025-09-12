import tensorflow as tf

def encode_ragged_tensor_to_variant(ragged_tensor):
    # Using `RaggedTensorToVariant` is deprecated and should be avoided.
    # Instead, serialize the RaggedTensor.
    serialized_ragged_tensor = tf.ragged.constant(ragged_tensor).to_variant()
    return serialized_ragged_tensor

# Example usage:
ragged_tensor = [[1, 2, 3], [4, 5], [], [6]]
encoded_variant = encode_ragged_tensor_to_variant(ragged_tensor)
print(encoded_variant)
