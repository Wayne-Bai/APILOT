
import tensorflow as tf
from tensorflow import summary

# create a session
sess = tf.Session()

# initialize variables
a = tf.Variable(1)
b = tf.Variable(2)
c = tf.add(a, b)

# create an operation to write the graph summary
summary_op = tf.summary.create_file_writer("/tmp/tensorboard")

# run the summary op on the session
sess.run(summary_op)

# close the session
sess.close()
