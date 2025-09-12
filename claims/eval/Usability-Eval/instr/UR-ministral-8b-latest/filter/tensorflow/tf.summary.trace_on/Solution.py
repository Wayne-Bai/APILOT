import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

# Define a simple computational graph
def create_graph():
    x = tf.placeholder(tf.float32, shape=(1, 2))
    y = tf.matmul(x, tf.ones([2, 2]))
    return x, y, y, tf.reduce_sum(y)

x, y1, y2, result = create_graph()

# Create a session to run the computation
with tf.compat.v1.Session() as sess:
    tf.compat.v1.initialize_all_variables()

    # Generate a trace
    traces.log(sess.graph)

    # Run the computation
    feed_dict = {x: [[1.0, 2.0]]}
    final_result = sess.run(result, feed_dict=feed_dict)

print("Final result:", final_result)
