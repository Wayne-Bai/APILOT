import tensorflow as tf

# Create a simple TensorFlow operation as an example
a = tf.constant(3.0, dtype=tf.float32)
b = tf.constant(4.0, dtype=tf.float32)
add_op = tf.add(a, b)

# Serialize the graph to a binary string in protobuf format
graph_def = tf.compat.v1.get_default_graph().as_graph_def()
serialized_graph = graph_def.SerializeToString()

# Print the serialized binary string
print(serialized_graph)
