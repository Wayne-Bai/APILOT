import tensorflow as tf

# Define the graph
graph = tf.Graph()

# Define the input tensor
input_tensor = tf.placeholder(tf.float32, shape=[None, None])

# Define the prediction tensor
pred = tf.raw_ops.ForwardsDataToOutputPort(input_tensor, output_port=0)

# Create a session to run the graph
with tf.Session(graph=graph) as sess:
    # Run the graph with some input data
    input_data = np.random.rand(10, 5)  # Replace this with your input data
    output_data = sess.run(pred, feed_dict={input_tensor: input_data})

    print(output_data)
