import tensorflow as tf

# Define the function
@tf.function
def my_function(x):
    y = tf.square(x)
    return y

# Create a TensorFlow graph
graph = tf.Graph()
with graph.as_default():
    # Define the input tensor
    x = tf.placeholder(tf.float32, shape=(None, 1))

    # Compile the function into a TensorFlow graph
    y = my_function(x)

    # Create a TensorFlow session
    sess = tf.Session(graph=graph)

    # Run the graph with some input
    input_data = [[1.0, 2.0, 3.0]]
    output_data = sess.run(y, feed_dict={x: input_data})

    print(output_data)
