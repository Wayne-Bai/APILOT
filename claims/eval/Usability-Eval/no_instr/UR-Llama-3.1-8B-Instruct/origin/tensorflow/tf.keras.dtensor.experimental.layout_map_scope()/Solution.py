# Importing the necessary libraries
import tensorflow as tf

# Creating a variable scope
with tf.variable_scope("MyScope"):
    # Initialize variables in the scope
    var1 = tf.Variable([1.0, 2.0], name="var1")
    var2 = tf.Variable([3.0, 4.0], name="var2")

# Testing the scope
print(tf.get_default_graph().get_collection(tf.GraphKeys.GLOBAL_VARIABLES))
print(tf.get_default_graph().get_collection(tf.GraphKeys.SCOPED_VARIABLES))

print(tf.get_default_graph().get_collection(tf.GraphKeys.GLOBAL_VARIABLES)[0].name == 'MyScope/var1:0')
print(tf.get_default_graph().get_collection(tf.GraphKeys.SCOPED_VARIABLES)[0].name == 'MyScope/var1:0')

# Resetting the scope to apply new settings
tf.reset_default_graph()
with tf.variable_scope("MyScope", reuse=True): 
    var1 = tf.Variable([1.0, 2.0], name="var1")
    var2 = tf.Variable([3.0, 4.0], name="var2")

# Testing the reuse flag
print(tf.get_default_graph().get_collection(tf.GraphKeys.GLOBAL_VARIABLES)[0].name == 'MyScope/var1:0')

# Removing the default variable scope
with tf.variable_scope("", reuse=True): 
    var1 = tf.Variable([1.0, 2.0], name="var1")

# Testing the reuse flag
# This will not throw error because it has same name inside the birth scope 
# since reuse=True has been set to 1
print(tf.get_default_graph().get_collection(tf.GraphKeys.GLOBAL_VARIABLES)[0].name == 'var1:0')
