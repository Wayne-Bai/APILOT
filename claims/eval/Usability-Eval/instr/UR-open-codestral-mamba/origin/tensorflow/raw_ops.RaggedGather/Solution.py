import tensorflow as tf

params = tf.constant([[[1, 1], [2, 2]],
                      [[3, 3], [4, 4]],
                      [[5, 5], [6, 6]]])
indices = tf.constant([[1], [2]])

output = tf.raw_ops.GatherRaggedSlices(params=params, indices=indices)
