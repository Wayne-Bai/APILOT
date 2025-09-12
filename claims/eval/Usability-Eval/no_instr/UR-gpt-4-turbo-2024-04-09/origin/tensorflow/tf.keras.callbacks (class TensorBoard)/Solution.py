import tensorflow as tf

# Define a simple computation graph
x = tf.constant([[1.0, 2.0], [3.0, 4.0]])
y = tf.constant([[5.0, 6.0], [7.0, 8.0]])
z = tf.matmul(x, y)

# Set up a TensorFlow session and run it
with tf.Session() as sess:
    # Initialize the FileWriter
    writer = tf.summary.FileWriter('logs/', sess.graph)

    # Run the operation
    result = sess.run(z)
    print("Result of matrix multiplication: \n", result)

    # Close the FileWriter
    writer.close()
