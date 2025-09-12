import tensorflow as tf

# Define the shape of your multi-dimensional array
dims = [4, 5, 6]  # Example: 4x5x6 array

# Generate a tensor of flat indices
indices = tf.range(tf.reduce_prod(dims))

# Convert the flat indices into a tuple of coordinate arrays
unraveled_coords = tf.unravel_index(indices, dims)

# Now, unraveled_coords is a tuple of three tensors, each with shape (4*5*6,),
# representing the indices in the three dimensions of the original array.

# Run the graph in a session
with tf.Session() as sess:
    coords = sess.run(unraveled_coords)
    print(coords)
