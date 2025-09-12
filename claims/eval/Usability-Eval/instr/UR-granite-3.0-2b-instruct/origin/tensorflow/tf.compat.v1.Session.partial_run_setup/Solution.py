import tensorflow as tf

# Create a graph
g = tf.Graph()

# Create placeholders for inputs
input1 = tf.placeholder(tf.float32, shape=[None, 3])
input2 = tf.placeholder(tf.float32, shape=[None, 3])

# Create a fetches for the operation
output = tf.matmul(input1, input2)

# Create a session
with g.as_default():
    sess = tf.Session()

# Initialize all variables
sess.run(tf.global_variables_initializer())

# Start a partial run
with g.as_default():
    output_result = sess.run(output, feed_dict={
        input1: np.random.rand(10, 3),
        input2: np.random.rand(10, 3)
    })

print("Output Result:\n", output_result)
