import tensorflow as tf

# Create a simple TensorFlow graph
g = tf.Graph()
with g.as_default():
    # Create a constant op
    const = tf.constant("Hello, World!")

# Serialize the graph to a binary string
serialized_graph = g.as_graph_def().SerializeToString()

# Serialize the constant tensor to a binary string
serialized_const = const.np_to_tensor().tobytes()

# Combine the serialized graph and constant tensor into a single binary string
serialized_data = serialized_graph + serialized_const

# Print the serialized binary string
print(serialized_data)
