import tensorflow as tf

# Define a ragged tensor
ragged_tensor = tf.ragged.constant([[1, 2, 3], [4, 5], [6]])

# Encode the ragged tensor into a variant tensor
encoded_variant = tf.raw_ops.RaggedTensorToVariant(rt_nested_splits=ragged_tensor.nested_row_splits, 
                                                   rt_dense_values=ragged_tensor.flat_values)

# To demonstrate: decode the variant tensor back to a ragged tensor
decoded_ragged_tensor = tf.RaggedTensor.from_variant(encoded_variant, ragged_rank=1)

# Check if the original and decoded tensors are the same
print('Original RaggedTensor:', ragged_tensor)
print('Decoded RaggedTensor:', decoded_ragged_tensor)
