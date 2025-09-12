import tensorflow as tf

indices = tf.constant([[0], [1]], dtype=tf.int64)
params = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

output = tf.gather(params, indices)

with tf.compat.v1.Session() as sess:
    result = sess.run(output)
    print(result)
