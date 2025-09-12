import tensorflow as tf

# Start a trace to record computation graphs and profiling information
with tf.profiler.experimental.start('logdir/profile'):
    # Define your model here.
    x = tf.random.uniform([100])
    w = tf.random.uniform([100])
    b = tf.random.uniform([1])

    logits = tf.add(tf.matmul(x, w), b)
    predictions = tf.nn.relu(logits)

    # Calculate loss and other metrics
    loss = tf.reduce_sum(tf.nn.relu_loss(predictions, tf.random.uniform([100])))

    # Print the summary of recorded data
    tf.print("Loss: ", loss.numpy())

# Stop the trace
tf.profiler.experimental.stop()
