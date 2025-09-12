import tensorflow as tf

# Define the input and output placeholders
x = tf.placeholder(tf.float32, shape=(None, 1))
y = tf.placeholder(tf.float32, shape=(None, 1))

# Define the model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Define the loss function
loss = tf.losses.mean_squared_error(labels=y, predictions=model(x))

# Define the optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)

# Define the training operation
train_op = optimizer.minimize(loss)

# Define the accuracy metric
accuracy = tf.metrics.mean_squared_error(labels=y, predictions=model(x))[1]

# Set up the session
with tf.Session() as sess:
    # Initialize the variables
    sess.run(tf.global_variables_initializer())

    # Run the training operation
    sess.run(train_op, feed_dict={x: X_train, y: y_train})

    # Calculate the accuracy
    acc = sess.run(accuracy, feed_dict={x: X_test, y: y_test})

    # Print the accuracy
    print('Accuracy:', acc)
