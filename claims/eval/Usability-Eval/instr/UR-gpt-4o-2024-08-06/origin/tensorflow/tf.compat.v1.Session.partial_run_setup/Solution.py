import tensorflow as tf

# Define the computational graph
x = tf.placeholder(tf.float32, shape=(None, 1), name='x')
y = tf.placeholder(tf.float32, shape=(None, 1), name='y')

# Define a simple linear model
W = tf.Variable(tf.random_normal([1, 1]), name='weights')
b = tf.Variable(tf.random_normal([1]), name='bias')
model = tf.add(tf.matmul(x, W), b, name='model')

# Define loss function
loss = tf.reduce_mean(tf.square(model - y), name='loss')

# Define optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Set up a session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Run the computation graph partially by specifying feeds and fetches
    feed_dict = {x: [[1.0], [2.0], [3.0]], y: [[2.0], [4.0], [6.0]]}
    for _ in range(100):
        _, loss_val = sess.run([train_op, loss], feed_dict=feed_dict)
        print(f"Loss: {loss_val}")

    # Fetch the final weights and bias
    final_weights, final_bias = sess.run([W, b])
    print(f"Weights: {final_weights}, Bias: {final_bias}")
