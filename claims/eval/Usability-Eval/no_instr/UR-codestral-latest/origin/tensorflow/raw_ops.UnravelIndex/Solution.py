import tensorflow as tf

# Define the shape of your tensor
shape = (4, 5, 6)

# Create a tensor with flat indices
indices = tf.range(tf.reduce_prod(shape))

# Convert the flat indices into coordinate arrays
coordinates = tf.unravel_index(indices, shape)

# Print the coordinates
with tf.Session() as sess:
    print(sess.run(coordinates))
