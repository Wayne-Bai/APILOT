import tensorflow as tf

# Define the graph
graph = tf.Graph()
with graph.as_default():
    # Placeholder for input data
    input_data = tf.placeholder(tf.float32, shape=[None, 10], name='input_data')
    
    # Some operations in the graph
    layer1 = tf.layers.dense(input_data, units=50, activation=tf.nn.relu, name='layer1')
    layer2 = tf.layers.dense(layer1, units=20, activation=tf.nn.relu, name='layer2')
    output = tf.layers.dense(layer2, units=1, activation=None, name='output')

# Create a session
with tf.Session(graph=graph) as sess:
    # Initialize variables
    sess.run(tf.global_variables_initializer())
    
    # Define feeds and fetches for partial run
    feeds = {'input_data:0': [[1.0] * 10]}
    fetches = ['layer1/BiasAdd:0', 'output/BiasAdd:0']
    
    # Perform partial run
    handle = sess.partial_run_setup(fetches, feeds.keys())
    result = sess.partial_run(handle, fetches[1], feed_dict=feeds)
    
    print("Partial run result:", result)
