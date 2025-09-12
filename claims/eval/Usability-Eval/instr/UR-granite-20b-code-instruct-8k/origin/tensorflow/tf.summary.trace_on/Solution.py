import tensorflow as tf

# Set up a TensorFlow session
sess = tf.Session()

# Create a TensorFlow debugger
debugger = tf.train.Debugger()

# Start the trace
debugger.begin()

# Run your TensorFlow computation graph
# ...

# End the trace
debugger.end()

# Close the TensorFlow session
sess.close()
