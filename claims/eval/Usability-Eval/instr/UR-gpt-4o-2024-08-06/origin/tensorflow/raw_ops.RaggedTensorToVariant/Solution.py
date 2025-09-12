import tensorflow as tf

# Define the RaggedTensor
values = tf.constant([1, 2, 3, 4, 5, 6])
row_splits = tf.constant([0, 2, 3, 6], dtype=tf.int64)
ragged_tensor = tf.RaggedTensor.from_row_splits(values, row_splits)

# Encode RaggedTensor into variant Tensor using tf.io.serialize_tensor
encoded_variant_tensor = tf.io.serialize_tensor(ragged_tensor)

# Print the encoded variant tensor
print("Encoded Variant Tensor:", encoded_variant_tensor)
