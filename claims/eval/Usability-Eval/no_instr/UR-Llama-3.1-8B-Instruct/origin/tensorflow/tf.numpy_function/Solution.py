import tensorflow as tf

# Define a function to be used as a TensorFlow op
def add_numbers(x, y):
    """A simple function to add two numbers."""
    return x + y

# Create a TensorFlow op from the function
@tf.function
def tensorflow_op(x, y):
    """Wraps the add_numbers function as a TensorFlow op."""
    return tf.py_function(add_numbers, [x, y], tf.float32)

# Create a TensorFlow graph and tensor
with tf.Graph().as_default():
    tf_x = tf.constant(2.0)
    tf_y = tf.constant(3.0)

    # Run the TensorFlow op
    result = tensorflow_op(tf_x, tf_y)

    # Initialize the TensorFlow session
    with tf.Session() as sess:
        # Print the result
        print(sess.run(result))
