import tensorflow as tf

# Define the RaggedTensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5]])

# Encode the RaggedTensor into a variant Tensor
encoded_tensor = tf.raw_ops.RaggedTensorToVariant(ragged_tensor=ragged_tensor)

# Print the encoded tensor
print(encoded_tensor)