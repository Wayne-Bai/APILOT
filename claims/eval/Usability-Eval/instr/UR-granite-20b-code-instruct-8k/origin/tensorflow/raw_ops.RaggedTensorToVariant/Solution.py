import tensorflow as tf
ragged_tensor = tf.ragged.constant([[1, 2], [3]])
variant_tensor = tf.raw_ops.RaggedTensorToVariant(ragged_tensor=ragged_tensor)
