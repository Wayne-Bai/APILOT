import tensorflow as tf

# Define the data and filter
x = tf.constant([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=tf.float32)
x = tf.reshape(x, [1, 3, 3, 1])
filter = tf.constant([[1]], dtype=tf.float32)
filter = tf.reshape(filter, [1, 1, 1, 1])

# Perform max pooling
max_pool = tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='VALID')

# Compute gradients
grads = tf.gradients(max_pool, [x])

# Print the gradients
with tf.Session() as sess:
    grads_val = sess.run(grads)
    print(grads_val)
