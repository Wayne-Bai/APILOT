import tensorflow as tf

# Define a RaggedTensor
rt = tf.ragged.constant([[1, 2], [3], [4, 5, 6]])

# Encode the RaggedTensor into a variant Tensor
variant_tensor = tf.raw_ops.RaggedTensorToVariant(ragged=rt)

# Print the variant tensor
print(variant_tensor)
