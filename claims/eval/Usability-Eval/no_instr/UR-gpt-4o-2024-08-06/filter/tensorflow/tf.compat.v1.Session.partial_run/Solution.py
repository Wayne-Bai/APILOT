import tensorflow as tf

# Creating a simple computational graph
a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
c = tf.add(a, b, name='c')

# Building a session to run the graph
class ExecutionManager:
    def __init__(self):
        # Define a session for computation
        self.sess = tf.compat.v1.Session()

    def run_graph(self):
        # Run the initial graph
        print("Initial run: ", self.sess.run(c))

    def continue_with_more_feeds_and_fetches(self, new_a, new_b):
        # Create placeholders for feed values
        a_ph = tf.compat.v1.placeholder(dtype=tf.int32, name='a_ph')
        b_ph = tf.compat.v1.placeholder(dtype=tf.int32, name='b_ph')

        # Update computational graph to accept placeholders
        updated_c = tf.add(a_ph, b_ph, name='updated_c')

        # Run the updated graph with new feed values
        result = self.sess.run(updated_c, feed_dict={a_ph: new_a, b_ph: new_b})
        print("Run with feed values ({} + {}): {}".format(new_a, new_b, result))

# Usage
manager = ExecutionManager()
manager.run_graph()
manager.continue_with_more_feeds_and_fetches(5, 7)  # Example new feed values
manager.continue_with_more_feeds_and_fetches(10, 15)
