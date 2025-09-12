import tensorflow as tf

# Define input variables
x = tf.placeholder(tf.float32, [None, 10])
y = tf.placeholder(tf.float32, [None])

# Define function to be compiled
def add_layer(inputs, hidden_size):
    W = tf.Variable(tf.truncated_normal([hidden_size, inputs.get_shape().as_list()[-1]], stddev=0.05))
    b = tf.Variable(tf.zeros([hidden_size]))
    layer_output = tf.add(tf.matmul(inputs, W), b)
    return layer_output

# Define the model
hidden = add_layer(x, 128)
hidden_relu = tf.nn.relu(hidden)
logits = add_layer(hidden_relu, 10)

# Define loss function
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits))

# Define optimization algorithm
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Create a training session and initiate
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

# Define a feed_dict to train the model
feed_dict = {x: np.random.uniform(-1, 1, (100, 10)),
             y: np.random.uniform(0, 1, (100))}

# Train the model
for i in range(100):
    _, c_loss = sess.run([train_op, loss], feed_dict=feed_dict)
    print(f"Step {i}, Loss: {c_loss}")
