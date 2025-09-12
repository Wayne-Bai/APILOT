
import tensorflow as tf

# Define a function that takes in a tensor and returns a tensor
def my_function(x):
    # Perform some operations on x, such as multiplication or addition
    return x * 2 + 1

# Create a TensorFlow graph from the function
graph = tf.Graph()
with graph.as_default():
    # Set the input tensor to be a placeholder
    x = tf.placeholder(dtype=tf.float32, shape=())
    # Call the function and get its output
    y = my_function(x)
    # Create a session to run the graph with
    sess = tf.Session()
    # Run the graph with the input tensor and get the output tensor
    result = sess.run(y, feed_dict={x: 3.0})

# Print the output tensor
print(result)
