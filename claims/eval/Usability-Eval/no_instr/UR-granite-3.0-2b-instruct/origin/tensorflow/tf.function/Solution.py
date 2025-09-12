import tensorflow as tf

# Define the function to be compiled
@tf.function
def my_function(x):
    y = tf.add(x, 2)
    return y

# Create a TensorFlow graph
graph = tf.Graph()

# Add the function to the graph
with graph.as_default():
    my_function = tf.function(my_function)

# Compile the graph
with tf.Session(graph=graph) as sess:
    sess.run(tf.global_variables_initializer())

# The graph is now callable
result = my_function(3)
print(result)
