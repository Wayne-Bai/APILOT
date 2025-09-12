
import tensorflow as tf

# Define the graph
graph = tf.Graph()

# Define the placeholder nodes
input_node = tf.placeholder(tf.float32, shape=[None], name='input')
output_node = tf.placeholder(tf.float32, shape=[None], name='output')

# Define the feed and fetch nodes
feed_dict = {input_node: [1., 2., 3.]}
fetches = [output_node]

# Create a session to run the graph
sess = tf.Session(graph=graph)

# Run the partial run with feeds and fetches
partial_run_results = sess.partial_run(feed_dict, fetches)

# Print the results
print(partial_run_results)
