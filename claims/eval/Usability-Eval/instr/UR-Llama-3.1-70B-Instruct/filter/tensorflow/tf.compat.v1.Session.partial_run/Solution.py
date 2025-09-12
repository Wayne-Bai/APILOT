# Importing the necessary libraries
import tensorflow as tf

# Creating a graph and a session
graph = tf.Graph()
sess = tf.Session(graph=graph)

# Placeholders for inputs
with graph.as_default():
    a = tf.placeholder(tf.float32, shape=[1])
    b = tf.placeholder(tf.float32, shape=[1])

    # Operation to add the inputs
    add = a + b

    # Initialize the variables
    init = tf.global_variables_initializer()

# Initialize the variables
sess.run(init)

# Fetch the result of the operation
result = sess.run(add, feed_dict={a: [5.0], b: [3.0]})

print("Result of a + b: ", result)

# Continues the execution with more feeds and fetches
result2 = sess.run(add, feed_dict={a: [10.0], b: [5.0]})

print("Result of a + b: ", result2)

# Close the session
sess.close()
