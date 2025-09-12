import tensorflow as tf

def encode_ragged_tensor_to_variant(ragged_tensor):
    # This function encodes a RaggedTensor into a variant tensor.
    variant_tensor = tf.raw_ops.RaggedTensorToVariant(
        rt_nested_splits=ragged_tensor.nested_row_splits,
        rt_dense_values=ragged_tensor.flat_values
    )
    return variant_tensor

# Example usage:
# Assuming the RaggedTensor is constructed as shown below
ragged_tensor = tf.RaggedTensor.from_row_splits(
    values=[3, 1, 4, 1, 5, 9, 2, 6],
    row_splits=[0, 4, 4, 7, 8]
)

encoded_variant = encode_ragged_tensor_to_variant(ragged_tensor)
print("Encoded variant tensor:", encoded_variant)
