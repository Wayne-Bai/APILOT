import tensorflow as tf

# Define a RaggedTensor
ragged_tensor = tf.ragged.constant([
    [1, 2, 3],
    [4, 5],
    [6]
])

# Encode the RaggedTensor into a Variant Tensor
encoded_variant = tf.io.serialize_tensor(ragged_tensor)

print(encoded_variant)
