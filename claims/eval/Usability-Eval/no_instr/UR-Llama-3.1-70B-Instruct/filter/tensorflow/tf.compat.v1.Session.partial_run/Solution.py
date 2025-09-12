# Importing necessary libraries
import tensorflow as tf

# Creating a graph
graph = tf.Graph()

# Defining placeholders for input and output
with graph.as_default():
    a = tf.placeholder(tf.float32, shape=[None])
    b = tf.placeholder(tf.float32, shape=[None])
    c = tf.add(a, b)

# Creating a session
sess = tf.Session(graph=graph)

# Feeding values for a and b in the first run
feed_dict = {a: [1, 2], b: [3, 4]}
fetches = [c]

# Running the session and fetching results
results = sess.run(fetches, feed_dict=feed_dict)
print(results)

# Continuing execution with more feeds and fetches
feed_dict = {a: [5, 6], b: [7, 8]}
fetches.append(tf.multiply(a, b))  # append another fetch

# Run the session with new feeds and fetches
results = sess.run(fetches, feed_dict=feed_dict)
print(results)
