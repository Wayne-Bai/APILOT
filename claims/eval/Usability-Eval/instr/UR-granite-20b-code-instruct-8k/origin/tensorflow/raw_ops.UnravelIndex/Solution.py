import tensorflow as tf

indices = tf.constant([[1, 1], [2, 2]], dtype=tf.int64)

indices_1 = tf.constant([1, 2], dtype=tf.int64)

coordinates = tf.raw_ops.DenseToDense(indices=indices, shape=[3, 3])

coordinates_1 = tf.raw_ops.DenseToDense(indices=indices_1, shape=[3, 3])

print(coordinates.numpy())
print(coordinates_1.numpy())
