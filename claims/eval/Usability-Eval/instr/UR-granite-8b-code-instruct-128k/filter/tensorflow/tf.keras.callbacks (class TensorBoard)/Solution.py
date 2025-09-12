import tensorflow as tf
# Enable visualizations for TensorBoard
tf.summary.FileWriter('/tmp/my-model', sess.graph)
