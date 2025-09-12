import tensorflow as tf

ragged_tensor = tf.ragged.constant([[1, 2, 3], [4], [5, 6]])
variant_tensor = tf.raw_ops.RaggedTensorToVariant(input=ragged_tensor)

with tf.Session() as sess:
    variant_tensor_val = sess.run(variant_tensor)

print(variant_tensor_val)
