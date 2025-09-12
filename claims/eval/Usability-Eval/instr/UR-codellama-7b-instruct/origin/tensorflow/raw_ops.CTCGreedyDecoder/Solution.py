
import tensorflow as tf

# Create a graph with a single input and output node
x = tf.placeholder(tf.float32, shape=(None, None, None))
y = tf.argmax(x, axis=1)

# Add the nodes to the default graph
sess = tf.Session()
sess.run([y], feed_dict={x: np.array([[0, 1], [2, 3]], dtype=np.float32)})
