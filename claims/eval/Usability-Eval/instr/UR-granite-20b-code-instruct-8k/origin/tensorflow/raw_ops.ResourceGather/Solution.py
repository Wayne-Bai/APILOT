import tensorflow as tf

resource = tf.Variable([1.0, 2.0, 3.0, 4.0, 5.0])
indices = tf.constant([0, 1, 3])

output = tf.raw_ops.ResourceGather(resource=resource, indices=indices, dtype=tf.float32)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    print(sess.run(output))
