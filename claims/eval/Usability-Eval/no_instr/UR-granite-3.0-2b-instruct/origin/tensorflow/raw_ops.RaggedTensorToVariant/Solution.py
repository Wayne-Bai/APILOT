import tensorflow as tf

# Define a RaggedTensor
ragged_tensor = tf.RaggedTensor.from_tensor([
    [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]
])

# Define a variant Tensor
variant_tensor = tf.variant.Variant(
    tf.variant.Variant.string,
    [
        "string1",
        "string2",
        "string3"
    ]
)

# Encode the RaggedTensor into a variant Tensor
encoded_tensor = tf.raw_ops.RaggedEncodeVariant(
    ragged_tensor,
    variant_tensor
)

# Print the encoded Tensor
print(encoded_tensor)
