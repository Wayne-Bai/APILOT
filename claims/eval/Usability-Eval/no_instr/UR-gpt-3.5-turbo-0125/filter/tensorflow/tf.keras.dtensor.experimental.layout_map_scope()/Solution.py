
import tensorflow as tf

def create_variables():
    with tf.variable_scope('my_variables'):
        var1 = tf.get_variable('var1', shape=[10], initializer=tf.random_normal_initializer())
        var2 = tf.get_variable('var2', shape=[5, 5], initializer=tf.truncated_normal_initializer())
        
    with tf.variable_scope('my_layout'):
        with tf.control_dependencies(None):
            tf.add_to_collection(tf.GraphKeys.GLOBAL_VARIABLES,
                                 tf.get_variable('var1', [10]))
            tf.add_to_collection(tf.GraphKeys.GLOBAL_VARIABLES,
                                 tf.get_variable('var2', [5, 5]))

create_variables()
