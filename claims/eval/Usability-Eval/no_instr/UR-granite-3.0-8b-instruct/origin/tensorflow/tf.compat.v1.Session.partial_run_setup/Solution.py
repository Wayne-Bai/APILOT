import tensorflow as tf

# Create a placeholder for input data
input_data = tf.placeholder(tf.float32, shape=[None, 10])

# Create a variable for the model parameters
weights = tf.Variable(tf.random_normal([10, 1]))
bias = tf.Variable(tf.random_normal([1]))

# Define the model
output = tf.add(tf.matmul(input_data, weights), bias)

# Create a session
sess = tf.Session()

# Initialize the variables
sess.run(tf.global_variables_initializer())

# Define the feeds and fetches
feeds = {input_data: [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]]}
fetches = [output]

# Run the partial graph
result = sess.run(fetches, feed_dict=feeds)

print(result)
