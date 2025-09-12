import tensorflow as tf

# Create a tensor
tensor = tf.constant([1, 2, 3, 4, 5])

# Store the input tensor in the state of the current session
with tf.Session() as sess:
    # Create a variable to store the tensor
    store_var = sess.graph.as_graph_element(tensor)

    # Get the handle to the stored tensor
    store_handle = store_var.eval()

    print("Stored tensor handle:", store_handle)
