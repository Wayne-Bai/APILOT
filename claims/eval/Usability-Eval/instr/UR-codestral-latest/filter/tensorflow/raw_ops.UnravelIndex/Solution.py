import tensorflow as tf

# Let's assume we have a 3D tensor of shape (3, 4, 5)
shape = [3, 4, 5]

# And we have an array of flat indices
indices = tf.constant([0, 15, 21, 30], dtype=tf.int32)

# Convert flat indices into a tuple of coordinate arrays
coords = tf.unravel_index(indices, shape)

# Display the result
with tf.Session() as sess:
    print(sess.run(coords))
