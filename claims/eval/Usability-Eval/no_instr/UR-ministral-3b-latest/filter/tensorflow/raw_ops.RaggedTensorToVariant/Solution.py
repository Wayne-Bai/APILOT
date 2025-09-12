import tensorflow as tf

# Example RaggedTensor
ragged_tensors = tf.ragged.constant([['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']])

# Create the variant tensor (ots/var)
variants = tf.ragged.constant([1.0, 2.0, 3.0])

# Encode the RaggedTensor into a TensorFlow variant tensor
encoded_tensor = tf.raw_ops.RaggedTensorToVariant([ragged_tensors, variants])

print(encoded_tensor)
