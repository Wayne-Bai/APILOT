
import tensorflow as tf

# Create a variable in the "current" scope (i.e., the scope where the code is being executed)
variable1 = tf.Variable(1, name='variable1')

with tf.name_scope('my_scope'):
    # Create a variable in a nested scope
    variable2 = tf.Variable(2, name='variable2')
    with tf.name_scope('my_other_scope'):
        # Create another variable in a deeper nested scope
        variable3 = tf.Variable(3, name='variable3')

print(tf.get_default_graph().as_graph_def())
