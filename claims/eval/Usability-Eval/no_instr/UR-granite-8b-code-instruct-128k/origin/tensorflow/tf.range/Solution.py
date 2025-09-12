import tensorflow as tf

# Create a sequence of numbers
seq = tf.range(10)

with tf.Session() as sess:
    print(sess.run(seq))
