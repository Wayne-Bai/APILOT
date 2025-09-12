import tensorflow as tf

# Assuming 'rt' is your RaggedTensor
rt = tf.RaggedTensor.from_row_lengths(...)

# Encode the RaggedTensor into a variant Tensor
variant_tensor = tf.raw_ops.EncodeRaggedTensor(rt)
