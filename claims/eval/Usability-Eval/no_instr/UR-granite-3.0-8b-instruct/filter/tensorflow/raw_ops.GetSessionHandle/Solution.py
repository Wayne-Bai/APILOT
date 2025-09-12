import tensorflow as tf

# Create a TensorFlow constant tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Create a session
with tf.Session() as sess:
    # Run the tensor in the session
    result = sess.run(tensor)

    # Print the result
    print(result)
