import tensorflow as tf

# Define a simple TensorFlow graph
builder = tf.GraphBuilder()
with builder.as_default():
    # Create a constant tensor
    const = builder.constant([1.0, 2.0, 3.0])

    # Create a session to run the graph
    with tf.Session(graph=builder.graph) as sess:
        # Serialize the graph to a binary string
        graph_def = sess.graph_def.SerializeToString()

        # Serialize the constant tensor to a binary string
        const_tensor_def = const.SerializeToString()

        # Combine the graph definition and constant tensor definition into a single binary string
        serialized_graph_and_tensor = graph_def + const_tensor_def

        # Print the serialized binary string
        print(serialized_graph_and_tensor)
