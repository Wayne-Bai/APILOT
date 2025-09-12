import tensorflow as tf

# Assuming 'compressed_dataset' is your compressed dataset tensor
# and 'uncompresses_shape' is the shape of the uncompressed dataset

# Define the uncompress operation
uncompress_op = tf.raw_ops.Uncompress(
    input=compressed_dataset,
    uncompresses_shape=uncompresses_shape,
    name='uncompress_op'
)

# Create a session to run the operation
with tf.Session() as sess:
    # Run the uncompress operation
    uncompressed_element = sess.run(uncompress_op)

    # The uncompressed_element tensor now contains the uncompressed dataset element
