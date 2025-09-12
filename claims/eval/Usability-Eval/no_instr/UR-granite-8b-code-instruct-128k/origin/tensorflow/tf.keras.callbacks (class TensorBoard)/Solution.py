
import tensorflow as tf

# Create a TensorFlow session
sess = tf.Session()

# Start TensorBoard visualization
tb = tf.summary.FileWriter('/tmp/tensorflow/logs', sess.graph)

# Train your model here

# Stop TensorBoard visualization
tb.close()
sess.close()
