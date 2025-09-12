import tensorflow as tf

# Set the TensorFlow graph
graph = tf.Graph()

# Example feeds
feed_dict = {
    'input': [1.0, 2.0, 3.0],
    'label': [1, 0, 1]
}

# Define operations
with graph.as_default():
    input_tensor = tf.placeholder(tf.float32, shape=[None])
    label_tensor = tf.placeholder(tf.int32, shape=[None])
    weights = tf.Variable(tf.random_normal([len(feed_dict['input']), 2]))
    bias = tf.Variable(tf.random_normal([2]))

    logits = tf.add(tf.matmul(input_tensor, weights), bias)
    prediction = tf.nn.softmax(logits)
    cross_entropy = tf.reduce_mean(-tf.log(tf.reduce_sum(tf.nn.softmax(logits) * label_tensor)))

    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
    train_op = optimizer.minimize(cross_entropy)

# Create session and run operations
with tf.Session(graph=graph) as sess:
    sess.run(tf.global_variables_initializer())
    # Feeding data for one iteration
    fetch_result = sess.run(train_op, feed_dict=feed_dict)
    print(fetch_result)
