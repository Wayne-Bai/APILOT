import tensorflow as tf

# Placeholder variables for the input data
x = tf.placeholder(tf.float32, shape=[None, 10])  # Assuming input data has 10 features
y = tf.placeholder(tf.float32, shape=[None, 5])   # Assuming output labels have 5 classes

# Example neural network layer
W = tf.Variable(tf.random_normal([10, 5]))
b = tf.Variable(tf.random_normal([5]))
output = tf.matmul(x, W) + b

# Example operation: Calculate the mean
mean_output = tf.reduce_mean(output)

# Initialize all variables
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    
    # Example feed data
    feed_dict_x = {
        x: [[1.0]*10, [2.0]*10, [3.0]*10],
        y: [[0, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 1, 0, 0]]
    }
    
    # Fetching the output and the mean of the output
    output_result, mean_result = sess.run([output, mean_output], feed_dict=feed_dict_x)
    
    print("Output of the network:", output_result)
    print("Mean of the output:", mean_result)
