
import tensorflow as tf

input_tensor = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=tf.float32)
filter_tensor = tf.constant([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=tf.float32)

output = tf.nn.conv2d(input=tf.expand_dims(tf.expand_dims(input_tensor, axis=0), axis=-1),
                      filters=tf.expand_dims(tf.expand_dims(filter_tensor, axis=-1), axis=-1),
                      strides=[1, 1, 1, 1],
                      padding='VALID')

print(output)
