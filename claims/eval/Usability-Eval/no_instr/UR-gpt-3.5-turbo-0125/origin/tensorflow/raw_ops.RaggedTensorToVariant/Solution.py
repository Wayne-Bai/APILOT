
import tensorflow as tf

rt = tf.ragged.constant([[1, 2], [3, 4, 5]])

variant_tensor = tf.raw_ops.EncodeRaggedTensor(rt)
print(variant_tensor)
