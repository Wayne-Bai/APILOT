import tensorflow as tf

# assuming we have a tensor of strings
data = tf.constant(['Hello', 'World', 'TensorFlow'])

# generating substring from tensor of strings
substr = tf.string.substr(data, 1, 3)

# display the substrings
with tf.Session() as sess:
    print(sess.run(substr))
