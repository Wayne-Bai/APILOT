import tensorflow as tf

def encode_ragged_tensor_to_variant(ragged_tensor):
    # Serialize RaggedTensor to a Variant tensor
    serialized_ragged = tf.RaggedTensor.from_nested_row_splits(
        flat_values=ragged_tensor.flat_values,
        nested_row_splits=ragged_tensor.nested_row_splits,
        validate=False
    )
    variant_tensor = tf.raw_ops.RaggedTensorToVariant(
        ragged_tensor=serialized_ragged,
        batched_input=False
    )
    return variant_tensor

# Create a RaggedTensor using tf.ragged.constant
ragged_tensor_input = tf.ragged.constant([[1, 2], [3, 4, 5]])

# Encode the RaggedTensor to a variant Tensor
encoded_variant_tensor = encode_ragged_tensor_to_variant(ragged_tensor_input)
print(encoded_variant_tensor)
