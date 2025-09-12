# Importing TensorFlow
import tensorflow as tf

# Create a new TensorFlow session
sess = tf.Session()

# Define placeholders for input data
input_data1 = tf.placeholder(tf.float32, shape=[None, 10], name='input1')
input_data2 = tf.placeholder(tf.float32, shape=[None, 20], name='input2')

# Define operations
output1 = tf.layers.dense(input_data1, 10, name='dense1')
output2 = tf.layers.dense(input_data2, 20, name='dense2')

# Define the feeds
feeds = {input_data1: [[1.0]*10], input_data2: [[2.0]*20]}

# Define the fetches
fetches = [output1, output2]

# Partial run setup
part_run_setup = sess.partial_run_setup(fetches=fetches, feeds=feeds)

# Run the session using partial run
fetches_results = sess.partial_run(part_run_setup, feed_dict=feeds)

# Print the results
for i, result in enumerate(fetches_results):
    print(f'Fetches Results {i+1}: {result}')
